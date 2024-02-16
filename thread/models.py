from django.db import models
from django.conf import settings
from dabubble_backend.messages.models import AbstractMessage


class Thread(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    members = models.ManyToManyField(User, related_name='channels', blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='started_chats', on_delete=models.CASCADE)

    def __str__(self):
        return f"Conversation between {self.created_by.username} and {self.member.username}"
    

class ThreadMessages(AbstractMessage):
    threadMessage = models.ForeignKey('Thread', related_name='messages', on_delete=models.CASCADE)

    def __str__(self):
        return f"Message by {self.sender.username} at {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"