from django.contrib import admin
from mailing.models import Mailing

@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = (
        "messages",
        "datetime_start",
        "datetime_finish",
        "period",
        "status",
    )