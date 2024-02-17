from rest_framework import serializers
from channel.models import Channel, ChannelMessage, ChannelThread,ChannelThreadMessage


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = '__all__'


class ChannelMesageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChannelMessage
        fields = '__all__'


class ChannelThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChannelThread
        fields = '__all__'


class ChannelThreadMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChannelThreadMessage
        fields = '__all__'