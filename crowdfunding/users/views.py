from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from .models import CustomUser
from .serializers import CustomUserSerializer, ChangePasswordSerializer, UpdateProfileSerializer

class CustomUserRegister (APIView):
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # token for new user
            token, created = Token.objects.get_or_create(user=user)
            response_data = serializer.data
            response_data.pop('password', None)
            response_data['token'] = token.key
            return Response(response_data, status=status.HTTP_201_CREATED)
        
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
        })

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

    def get_object(self):
        return self.request.user

# update authenticated user password
    
    def perform_update(self, serializer):
        user=self.get_object()
        serializer.save()

# delete old token and create new when password updated
        Token.objects.filter(user=user).delete()
        new_token = Token.objects.create(user=user)

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            token, created = Token.objects.get_or_create(user=self.get_object())
            response.data['token'] = token.key
        return response 

class UpdateProfileView (UpdateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateProfileSerializer

    def get_object(self):
        return self.request.user
    
    def update (self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

class DeleteProfileView (APIView):
    permission_classes = (IsAuthenticated,)
    
    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise Http404

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        if request.user != user and not request.user.is_superuser:
            return Response(status=status.HTTP_403_FORBIDDEN)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)