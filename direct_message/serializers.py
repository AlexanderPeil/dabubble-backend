from rest_framework import serializers
from direct_message.models import DirectChat, DirectMessages, DirectChatThread, DirectChatThreadMessage


class DirectChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectChat
        fields = '__all__'


class DirectMessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectMessages
        fields = '__all__'


class DirectChatThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectChatThread
        fields = '__all__'


class DirectChatThreadMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectChatThreadMessage
        fields = '__all__'