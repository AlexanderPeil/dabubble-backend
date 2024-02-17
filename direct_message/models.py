from django.db import models
from django.conf import settings
from conversations.models import AbstractMessage


class DirectChat (models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    member = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='direct_chats', on_delete=models.CASCADE)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='started_chats', on_delete=models.CASCADE)

    def __str__(self):
        return f"Conversation between {self.created_by.username} and {self.member.username}"
    

class DirectMessages(AbstractMessage):
    directChat  = models.ForeignKey('DirectChat', related_name='messages', on_delete=models.CASCADE)

    def __str__(self):
        return f"Message by {self.created_by.username} at {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"
    
class DirectChatThread(models.Model):
    direct_chat = models.ForeignKey(DirectChat, related_name='threads', on_delete=models.CASCADE)


class DirectChatThreadMessage(AbstractMessage):
    thread = models.ForeignKey('DirectChatThread', on_delete=models.CASCADE, related_name='direct_chat_thread_messages')

    def __str__(self):
        return f"Thread message from {self.created_by.username} at {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"
