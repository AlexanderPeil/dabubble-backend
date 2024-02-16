from django.db import models
from django.conf import settings
from dabubble_backend.messages.models import AbstractMessage


class DirectChat (models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    member = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='direct_chats', on_delete=models.CASCADE)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='started_chats', on_delete=models.CASCADE)

    def __str__(self):
        return f"Conversation between {self.created_by.username} and {self.member.username}"
    

class DirectMessages(AbstractMessage):
    directChat  = models.ForeignKey('DirectChat', related_name='messages', on_delete=models.CASCADE)

    def __str__(self):
        return f"Message by {self.sender.username} at {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"