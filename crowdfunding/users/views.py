from rest_framework import status, generics
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
            return Response(response_data)
        
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
    
class ChangePasswordView(generics.UpdateAPIView):

        queryset = CustomUser.objects.all()
        permission_classes = (IsAuthenticated,)
        serializer_class = ChangePasswordSerializer
