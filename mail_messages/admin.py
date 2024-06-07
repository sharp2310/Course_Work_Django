from django.contrib import admin

from mail_messages.models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('message_subject', 'text')