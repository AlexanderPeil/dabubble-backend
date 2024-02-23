from rest_framework import serializers
from channel.models import Channel, ChannelMessage, ChannelThread,ChannelThreadMessage
from django.contrib.auth import get_user_model

User = get_user_model()



class ChannelSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')
    member_ids = serializers.ListField(child=serializers.IntegerField(), write_only=True, required=False)

    class Meta:
        model = Channel
        fields = ['id', 'created_at', 'title', 'description', 'members', 'created_by', 'member_ids']
        read_only_fields = ['id', 'created_at', 'members', 'created_by']

    def create(self, validated_data):
        member_ids = validated_data.pop('member_ids', [])
        # creator = self.context['request'].user
        # if creator.id not in member_ids:
        #     member_ids.append(creator.id)
        channel = Channel.objects.create(**validated_data)
        channel.members.set(User.objects.filter(id__in=member_ids))
        return channel


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