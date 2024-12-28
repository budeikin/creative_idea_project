from accounts.models import CustomUser
from django.contrib.auth import authenticate
from rest_framework import serializers


class RegisterionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'role']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'role']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(
            email=validated_data['email'],
            role=validated_data['role']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
