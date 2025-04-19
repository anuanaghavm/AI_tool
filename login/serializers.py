from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import send_mail
from django.conf import settings

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'phone_number', 'password']  # ✅ no 'role' here

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    role = serializers.CharField(read_only=True)  # ✅ include role

    def validate(self, data):
        try:
            user = User.objects.get(email=data['email'])
            if user.password == data['password']:  # Insecure, but as per your model
                return {
                    'email': user.email,
                    'name': user.name,
                    'id': user.id,
                    'role': user.role  # ✅ include role in output
                }
        except User.DoesNotExist:
            pass
        raise serializers.ValidationError("Invalid credentials")


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError("No user found with this email address")
        return value

class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    phone_number = serializers.CharField()
    new_password = serializers.CharField(min_length=6, write_only=True)

    def validate(self, data):
        try:
            user = User.objects.get(email=data['email'], phone_number=data['phone_number'])
        except User.DoesNotExist:
            raise serializers.ValidationError("No user found with this email and phone number combination")
        return data
