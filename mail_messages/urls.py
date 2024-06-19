from django.urls import path

from mail_messages.views import (
    MessageListView,
    MessageCreateView,
    MessageDetailView,
    MessageUpdateView,
    MessageDeleteView,
)

app_name = "mail_messages"

urlpatterns = [
    path("list/", MessageListView.as_view(), name="message_list"),
    path("create/", MessageCreateView.as_view(), name="message_create"),
    path("view/<int:pk>", MessageDetailView.as_view(), name="message_detail"),
    path("edit/<int:pk>", MessageUpdateView.as_view(), name="message_edit"),
    path("delete/<int:pk>", MessageDeleteView.as_view(), name="message_delete"),
]