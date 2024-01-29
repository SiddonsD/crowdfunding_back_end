from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create(
            username = validated_data["username"], 
            first_name = validated_data["first_name"],
            last_name = validated_data["last_name"],
            email = validated_data["email"]
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
# user update profile feature modified from https://medium.com/django-rest/django-rest-framework-change-password-and-update-profile-1db0c144c0a3
    
class UpdateUserSeralizer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        Model = CustomUser
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password']
        extra_kwargs = {'password': {'read_only': True}}

    def validate_email (self, value):
        user = self.context['request'].user
        if CustomUser.objects.exclude(pk=user.pk).filter(email=value).exists():
            raise serializers.ValidationError({"email": "This email is already exists."})
        return value
    
    def validate_username(self, value):
        user = self.context['request'].user
        if CustomUser.objects.exclude(pk=user.pk).filter(username=value).exists():
            raise serializers.ValidationError({"username": "This username is already in use."})
        return value
    
    def update(self, instance, validated_data):
        instance.first_name = validated_data['first_name']
        instance.last_name = validated_data['last_name']
        instance.email = validated_data['email']
        instance.username = validated_data['username']

        instance.save()

        return instance 

