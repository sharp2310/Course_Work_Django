from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)

from schedule.forms import NewsletterForm
from schedule.models import Newsletter, CREATE, Client, TextForNewsletter
from schedule.services import send_mailing


class NewsletterListView(LoginRequiredMixin, ListView):
    model = Newsletter
    permission_required = "schedule.can_view_all_newsletter"
    success_url = reverse_lazy("schedule:newsletter_list")

    def get_queryset(self):
        user = self.request.user
        company = user.user_company

        if user.has_perm("schedule.can_view_all_newsletter") or user.is_superuser:
            return Newsletter.objects.all()

        else:
            newsletters = (
                Newsletter.objects.filter(clients__company=company)
                .prefetch_related("clients__company", "message")
                .distinct()
            )
            return newsletters


class NewsletterLDetailView(LoginRequiredMixin, DetailView):
    model = Newsletter
    context_object_name = "newsletter"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        user = self.request.user
        if (
            user.is_superuser
            or (obj.clients.filter(company=user.user_company).exists())
            or user.is_staff
        ):
            return obj
        else:
            raise Http404("You do not have permission to view this newsletter.")

    def get_success_url(self):
        return reverse("schedule:newsletter_detail")


class NewsletterCreateView(LoginRequiredMixin, CreateView):
    model = Newsletter
    form_class = NewsletterForm

    success_url = reverse_lazy("schedule:newsletter_list")

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        user = self.request.user
        company = user.user_company

        form.fields["clients"].queryset = Client.objects.filter(company=company)
        form.fields["message"].queryset = TextForNewsletter.objects.filter(
            company=company
        )
        return form

    def form_valid(self, form):
        newsletter = form.save(commit=False)

        selected_clients = form.cleaned_data.get("clients")
        selected_messages = form.cleaned_data.get("message")
        selected_start_time = form.cleaned_data.get("start_time")

        newsletter.status_of_newsletter = CREATE
        newsletter.start_time = selected_start_time

        user = self.request.user
        newsletter.owner = user
        newsletter.save()

        newsletter.clients.set(selected_clients)
        newsletter.message = selected_messages

        send_mailing(newsletter)

        return super().form_valid(form)


class NewsletterUpdateView(LoginRequiredMixin, UpdateView):
    model = Newsletter
    form_class = NewsletterForm

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        user = self.request.user
        company = user.user_company

        form.fields["clients"].queryset = Client.objects.filter(company=company)
        form.fields["message"].queryset = TextForNewsletter.objects.filter(
            company=company
        )
        return form

    def get_success_url(self):
        return reverse("schedule:newsletter_list")

    def form_valid(self, form):
        newsletter = form.save(commit=False)

        selected_clients = form.cleaned_data.get("clients")
        selected_messages = form.cleaned_data.get("message")
        selected_start_time = form.cleaned_data.get("start_time")

        newsletter.status_of_newsletter = CREATE
        newsletter.start_time = selected_start_time

        user = self.request.user
        newsletter.owner = user
        newsletter.save()

        newsletter.message = selected_messages
        newsletter.clients.set(selected_clients)

        send_mailing(newsletter)

        return super().form_valid(form)


class NewsletterDeleteView(LoginRequiredMixin, DeleteView):
    model = Newsletter

    def get_success_url(self):
        return reverse("schedule:newsletter_list")