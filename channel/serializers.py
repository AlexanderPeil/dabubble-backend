from rest_framework import serializers
from channel.models import Channel, ChannelMessage, ChannelThread,ChannelThreadMessage
from django.contrib.auth import get_user_model

User = get_user_model()



from rest_framework import serializers

class ChannelSerializer(serializers.ModelSerializer):
    created_by_full_name = serializers.SerializerMethodField()  # Änderung hier
    member_ids = serializers.ListField(child=serializers.IntegerField(), write_only=True, required=False)

    class Meta:
        model = Channel
        fields = ['id', 'created_at', 'title', 'description', 'members', 'created_by', 'member_ids', 'created_by_full_name']  # Füge created_by_full_name hinzu
        read_only_fields = ['id', 'created_at', 'members', 'created_by']

    def get_created_by_full_name(self, obj):  # Stelle sicher, dass der Methodenname mit get_<Feldname> beginnt
        return f"{obj.created_by.first_name} {obj.created_by.last_name}"

    def create(self, validated_data):
        member_ids = validated_data.pop('member_ids', [])
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