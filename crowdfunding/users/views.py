from django.contrib.auth.models import AbstractUser
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CustomUser
from .serializers import CustomUserSerializer, ChangePasswordSerializer



class CustomUserRegister (APIView):
    
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            response_data = serializer.data
            response_data.pop('password', None)
            return Response(response.data)
        
        return Response (serializer.errors)

class CustomUserList (APIView):

    def get(self, request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)


class CustomUserDetail (APIView):

    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)
    
class ChangePasswordView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get_object(self):
        return self.request.user
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = ChangePasswordSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
# validate users existing password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response ({"old_password": ["Password is incorrect."]}, status=status.HTTP_400_BAD_REQUEST)
            
# if old password a match, user sets new password
            self.object.set_password(serializer.data.get("new_password"))
            self.object()
            return Response({"success": "Your password has been successfully updated"}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

            

