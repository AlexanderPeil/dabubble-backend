from django.contrib import admin
from direct_message.models import DirectChat, DirectMessages, DirectChatThread, DirectChatThreadMessage 


admin.site.register(DirectChat)
admin.site.register(DirectMessages)
admin.site.register(DirectChatThread)
admin.site.register(DirectChatThreadMessage)