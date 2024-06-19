from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Пользователь"""

    avatar = models.ImageField(
        upload_to="users/avatars/", blank=True, null=True, verbose_name="аватар"
    )
    phone = models.CharField(
        max_length=30, blank=True, null=True, verbose_name="телефон"
    )

    is_manager = models.BooleanField(
        default=False, blank=True, null=True, verbose_name="менеджер"
    )  # права менеджера

    username = None
    email = models.EmailField(unique=True, verbose_name="почта")

    token = models.CharField(
        max_length=100, verbose_name="Токен", blank=True, null=True
    )

    id = models.IntegerField(
        primary_key=True, default=3, editable=False, verbose_name="id_пользователя"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []