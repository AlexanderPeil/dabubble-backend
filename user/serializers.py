from rest_framework import serializers
from user.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class meta:
        model = CustomUser
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True},
            'is_verified': {'read_only': True},
        }


class ResetPasswordSerializer(serializers.Serializer):
    token = serializers.CharField()
    password = serializers.CharField()