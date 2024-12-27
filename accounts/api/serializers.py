from accounts.models import CustomUser
from django.contrib.auth import authenticate
from rest_framework import serializers


class RegisterionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'role']
