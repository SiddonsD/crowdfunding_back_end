from django.contrib.auth.password_validation import validate_password
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
    
# https://medium.com/django-rest/django-rest-framework-change-password-and-update-profile-1db0c144c0a3
    
class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ('old_password', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields do not match."})
        
        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"old_password": "Password is not correct"})
        return value
    
    def update(self, instance, validated_data):

        instance.set_password(validated_data['password'])
        instance.save()

        return instance