from dataclasses import field
from django.contrib.auth.models import Group
from rest_framework import serializers
from .models import User

class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name', 'birth_date', 'member_position']
    
    def create(self, validated_data):
        user = User.objects.create_user(username=
            validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            member_position=validated_data['member_position']
            )
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

class LoginSerializer(serializers.ModelSerializer):

    password = serializers.CharField(max_length=128, min_length=2, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'token')

        read_only_fields = ['token']