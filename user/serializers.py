from rest_framework import serializers
from user.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        # fields = ['id', 'password', 'first_name', 'last_name', 'email', 'is_verified', 'is_online', 'photo', 'username']
        extra_kwargs = {
            'password': {'write_only': True},
            'is_verified': {'read_only': True},
        }


class ResetPasswordSerializer(serializers.Serializer):
    token = serializers.CharField()
    password = serializers.CharField()