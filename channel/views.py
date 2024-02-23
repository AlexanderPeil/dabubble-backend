from django.shortcuts import render

from .serializers import (
    ChannelSerializer,
    ChannelMesageSerializer,
    ChannelThreadSerializer,
    ChannelThreadMessageSerializer
)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from rest_framework.authtoken.models import Token

from user.models import CustomUser
from .models import (
    Channel,
    ChannelMessage,
    ChannelThread,
    ChannelThreadMessage
)


class ChannelViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ChannelSerializer

    def get_queryset(self):
        return Channel.objects.all().order_by("title")
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save()