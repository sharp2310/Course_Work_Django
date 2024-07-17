import secrets

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, ListView, DetailView

from config.settings import DEFAULT_FROM_EMAIL, EMAIL_HOST_USER
from users.form import UsersRegisterForm
from users.models import User


class UserCreateView(CreateView):
    model = User
    form_class = UsersRegisterForm
    success_url = reverse_lazy("schedule:home")

    def form_valid(self, form):
        user = form.save(commit=False)
        user.token = secrets.token_hex(7)
        user.save()

        host = self.request.get_host()
        url = f"http://{host}/users/confirm-register/{user.token}/"

        send_mail(
            subject="Hi! You need to confirm your registration",
            message=f"Click here if it was you: {url}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )

        return super().form_valid(form)


class PasswortResetView(FormView):
    model = User
    template_name = "passwort_reset_view.html"
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        email_form = form.cleaned_data("email")
        user = User.objects.get(email=email_form)

        new_password = User.objects.make_random_password()
        user.set_password(new_password)
        user.save()
        send_mail(
            subject="New password",
            message=f"Here: {new_password}",
            from_email=DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
        )
        return super().form_valid(form)


class UserListView(LoginRequiredMixin, ListView):
    model = User
    success_url = reverse_lazy("users:user_list")


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    success_url = reverse_lazy("users:user_detail")