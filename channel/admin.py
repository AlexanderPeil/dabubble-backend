from django.contrib import admin
from channel.models import Channel, ChannelMessage, ChannelThread, ChannelThreadMessage


class ChannelAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'created_by')

admin.site.register(Channel, ChannelAdmin)


# admin.site.register(Channel)
admin.site.register(ChannelMessage)
admin.site.register(ChannelThread)
admin.site.register(ChannelThreadMessage)