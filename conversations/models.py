from django.db import models
from django.conf import settings


class AbstractMessage(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    emotes = models.JSONField(default=dict)  # Speichert Emojis und deren Anzahl
    files = models.FileField(upload_to='channel_messages/', blank=True, null=True)

    def __str__(self):
        return self.created_at.strftime('%Y-%m-%d %H:%M:%S')
