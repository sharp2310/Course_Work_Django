from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from mail_messages.forms import MessageForm
from mail_messages.models import Message
from mailing.views import ManagerOrOwnerRequiredMixin, OwnerRequiredMixin


class MessageListView(ListView):
    """Контроллер просмотра списка сообщений для рассылки"""

    model = Message
    paginate_by = 6
    ordering = ["-id"]

    def dispatch(self, request, *args, **kwargs):  # запрет доступа без авторизации
        if self.request.user.is_anonymous:
            return redirect("mailing:access_error")
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(
        self, *args, **kwargs
    ):  # # отображение только тех сообщений, которые созданы пользователем
        queryset = super().get_queryset()
        if not self.request.user.is_manager:  # менеджеру доступны все сообщения
            queryset = queryset.filter(owner=self.request.user.pk)
        return queryset


class MessageCreateView(LoginRequiredMixin, CreateView):
    """Контроллер создания сообщения для рассылки"""

    model = Message
    form_class = MessageForm
    success_url = reverse_lazy("mail_messages:message_list")

    def form_valid(self, form):
        if form.is_valid():
            product = form.save()
            product.owner = self.request.user
            product.save()

        return super().form_valid(form)


class MessageDetailView(ManagerOrOwnerRequiredMixin, DetailView):
    """Контроллер просмотра отдельного сообщения для рассылки"""

    model = Message


class MessageUpdateView(OwnerRequiredMixin, UpdateView):
    """Контроллер редактирования сообщения для рассылки"""

    model = Message
    form_class = MessageForm
    success_url = reverse_lazy("mail_messages:message_list")


class MessageDeleteView(OwnerRequiredMixin, DeleteView):
    """Контроллер удаления сообщения для рассылки"""

    model = Message
    success_url = reverse_lazy("mail_messages:message_list")