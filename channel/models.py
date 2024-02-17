from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from conversations.models import AbstractMessage

User = get_user_model()


class Channel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    members = models.ManyToManyField(User, related_name='channels', blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class ChannelMessage(AbstractMessage):
    channel = models.ForeignKey('channel.Channel', related_name='messages', on_delete=models.CASCADE)

    def __str__(self):
        return f"Message by {self.created_by.username} in {self.channel.title} at {self.created_at}"
    

class ChannelThread(models.Model):
    channel = models.ForeignKey(Channel, related_name='threads', on_delete=models.CASCADE)


class ChannelThreadMessage(AbstractMessage):
    thread = models.ForeignKey('ChannelThread', on_delete=models.CASCADE, related_name='channel_thread_messages')

    def __str__(self):
        return f"Thread message from {self.created_by.username} at {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"

