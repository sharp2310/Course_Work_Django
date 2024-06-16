import random
import string
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, FormView, ListView
from config import settings
from config.settings import DEFAULT_FROM_EMAIL
from mailing.views import ManagerRequiredMixin
from users.forms import (
    RegisterCreationForm,
    UserProfileForm,
    PasswordResetForm,
    UserStatusForm,
)
from users.models import User
class RegisterView(CreateView):
    """Контроллер создания пользователя"""
    model = User
    form_class = RegisterCreationForm
    template_name = "users/register.html"
    success_url = reverse_lazy("users:check_email")
    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        send_mail(
            "Подтвердите свою почту",
            f"Ваша учетная запись подтверждена!\nПерейдите по ссылке - http://127.0.0.1:8000/users/verify/{user.pk}",
            settings.EMAIL_HOST_USER,
            [user.email],
            fail_silently=False,
        )
        return super().form_valid(form)
def verify(request, id_user):
    user = get_object_or_404(User, id=id_user)
    if user.is_active is False:
        user.is_active = True
        user.save()
        return HttpResponseRedirect(reverse_lazy("users:login"))
    return HttpResponseRedirect(reverse_lazy("users:register"))
def check_email(request):
    return render(request, "users/check_email.html")
class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy("mailing:home")
    def get_object(self, queryset=None):
        return self.request.user
class PasswordResetView(FormView):
    model = User
    form_class = PasswordResetForm
    template_name = "users/password_reset_form.html"
    success_url = reverse_lazy("users:login")
    def form_valid(self, form):
        email_form = form.cleaned_data["email"]
        try:
            user = User.objects.get(email=email_form)
        except User.DoesNotExist:
            return render(
                self.request,
                self.template_name,
                {"form": form, "error": "Пользователь с таким email-ом не найден"},
            )
        new_pass = "".join(random.choices(string.ascii_letters + string.digits, k=8))
        user.set_password(new_pass)
        user.save()
        send_mail(
            subject="Новый пароль",
            message=f"Ваш новый пароль: {new_pass}",
            from_email=DEFAULT_FROM_EMAIL,
            recipient_list=[user.emails],
            fail_silently=False,
        )
        return super().form_valid(form)
class UserUpdateView(ManagerRequiredMixin, UpdateView):
    """Контроллер редактирования пользователя"""
    model = User
    form_class = UserStatusForm
    success_url = reverse_lazy("users:user_list")
class UserListView(ListView):
    model = User
    paginate_by = 9
    ordering = ["-id"]
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_anonymous:
            return redirect("mailing:access_error")
        elif not self.request.user.is_manager:
            return redirect("mailing:access_error")
        return super().dispatch(request, *args, **kwargs)