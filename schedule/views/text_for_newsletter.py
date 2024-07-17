from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from schedule.models import TextForNewsletter


class TextForNewsletterListView(LoginRequiredMixin, ListView):
    model = TextForNewsletter

    def get_queryset(self):
        user = self.request.user

        if user.is_superuser:
            return TextForNewsletter.objects.all()
        else:
            return TextForNewsletter.objects.filter(company=user.user_company)


class TextForNewsletterCreateView(LoginRequiredMixin, CreateView):
    model = TextForNewsletter
    fields = (
        "subject",
        "text",
    )
    success_url = reverse_lazy("schedule:textfornewsletter_list")

    def form_valid(self, form):
        user = self.request.user
        form.save(commit=False)
        form.instance.company = user.user_company

        return super().form_valid(form)


class TextForNewsletterUpdateView(LoginRequiredMixin, UpdateView):
    model = TextForNewsletter
    fields = (
        "subject",
        "text",
    )

    def dispatch(self, request, *args, **kwargs):
        user = self.request.user
        if not (user.user_company == self.get_object().company or user.is_superuser):
            return HttpResponseForbidden("Go out!")
        else:
            return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("schedule:textfornewsletter_list")


class TextForNewsletterDeleteView(LoginRequiredMixin, DeleteView):
    model = TextForNewsletter

    def dispatch(self, request, *args, **kwargs):
        user = self.request.user
        if not (user.user_company == self.get_object().company or user.is_superuser):
            return HttpResponseForbidden("Go out!")
        else:
            return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("schedule:textfornewsletter_list")