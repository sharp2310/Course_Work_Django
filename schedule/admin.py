from django.contrib import admin

from schedule.models import Client, TextForNewsletter, Newsletter, Log


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "contact_email",
        "fullname",
        "comment",
    )


@admin.register(TextForNewsletter)
class TextForNewsletterAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "subject",
        "text",
    )


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "start_time",
        "end_time",
        "frequency",
        "status_of_newsletter",
        "is_active",
    )


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "status_of_last_attempt",
        "server_response",
        "time_attempt",
    )