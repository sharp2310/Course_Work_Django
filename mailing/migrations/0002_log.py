import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("customers", "0001_initial"),
        ("mailing", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Log",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "try_time",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="дата и время последней попытки"
                    ),
                ),
                (
                    "try_status",
                    models.CharField(
                        choices=[("success", "успешно"), ("fail", "не успешно")],
                        max_length=50,
                        verbose_name="статус попытки",
                    ),
                ),
                (
                    "server_answer",
                    models.CharField(
                        blank=True,
                        max_length=250,
                        null=True,
                        verbose_name="ответ почтового сервера",
                    ),
                ),
                (
                    "clients",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="customers.customer",
                        verbose_name="контакты клиентов",
                    ),
                ),
                (
                    "mailing",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mailing.mailing",
                        verbose_name="рассылка",
                    ),
                ),
            ],
            options={
                "verbose_name": "лог",
                "verbose_name_plural": "логи",
            },
        ),
    ]