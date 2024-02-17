from django.contrib import admin
from channel.models import Channel, ChannelMessage, ChannelThread, ChannelThreadMessage


admin.site.register(Channel)
admin.site.register(ChannelMessage)
admin.site.register(ChannelThread)
admin.site.register(ChannelThreadMessage)