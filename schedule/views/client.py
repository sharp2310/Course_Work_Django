from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from schedule.models import Client


class ClientsListView(LoginRequiredMixin, ListView):
    model = Client

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Client.objects.all()
        else:
            return Client.objects.filter(company=user.user_company)


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    fields = (
        "contact_email",
        "fullname",
        "comment",
    )
    success_url = reverse_lazy("schedule:client_list")

    def form_valid(self, form):
        user = self.request.user
        form.save(commit=False)
        form.instance.company = user.user_company

        return super().form_valid(form)


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    fields = (
        "contact_email",
        "fullname",
        "comment",
    )

    def get_success_url(self):
        return reverse("schedule:client_list")

    def dispatch(self, request, *args, **kwargs):
        user = self.request.user
        if not (user.is_staff or user.is_superuser):
            return HttpResponseForbidden("Go out!")
        else:
            return super().dispatch(request, *args, **kwargs)


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client

    def get_success_url(self):
        return reverse("schedule:client_list")

    def dispatch(self, request, *args, **kwargs):
        user = self.request.user
        if not (user.is_staff or user.is_superuser):
            return HttpResponseForbidden("Go out!")
        else:
            return super().dispatch(request, *args, **kwargs)