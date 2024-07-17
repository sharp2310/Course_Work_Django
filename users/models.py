from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Company(models.Model):
    company_name = models.CharField(max_length=150, verbose_name="Название компании")

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"


class User(AbstractUser):
    username = None
    email = models.EmailField(max_length=50, verbose_name="Email", unique=True)
    user_company = models.ForeignKey(
        Company,
        on_delete=models.SET_NULL,
        verbose_name="Компания",
        null=True,
        blank=True,
    )
    phone = PhoneNumberField(unique=True, verbose_name="Телефон", blank=True, null=True)
    city = models.CharField(max_length=150, verbose_name="Город")
    token = models.CharField(
        max_length=200, verbose_name="Token", blank=True, null=True
    )
    is_active = models.BooleanField(default=False)
    avatar = models.ImageField(
        verbose_name="Аватар", upload_to="users/", blank=True, null=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

        permissions = [
            ("can_block", "Можно заблокировать"),
            ("can_view_users", "Можно просматривать пользователей"),
        ]