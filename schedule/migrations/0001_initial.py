from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Client",
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
                    "contact_email",
                    models.EmailField(
                        help_text="Введите свой email",
                        max_length=50,
                        unique=True,
                        verbose_name="Email",
                    ),
                ),
                ("fullname", models.TextField(verbose_name="фио")),
                (
                    "comment",
                    models.CharField(max_length=250, verbose_name="комментарий"),
                ),
            ],
            options={
                "verbose_name": "Клиент",
                "verbose_name_plural": "Клиенты",
            },
        ),
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
                    "time_attempt",
                    models.DateTimeField(
                        auto_now_add=True,
                        null=True,
                        verbose_name="дата и время последней попытки",
                    ),
                ),
                (
                    "status_of_last_attempt",
                    models.BooleanField(
                        blank=True, null=True, verbose_name="Статус попытки"
                    ),
                ),
                (
                    "server_response",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Ответ почтового сервера",
                    ),
                ),
            ],
            options={
                "verbose_name": "Лог отправки сообщения",
                "verbose_name_plural": "Логи отправки сообщений",
            },
        ),
        migrations.CreateModel(
            name="Newsletter",
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
                    "start_time",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="время начала рассылки"
                    ),
                ),
                (
                    "end_time",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="время окончания рассылки"
                    ),
                ),
                (
                    "frequency",
                    models.CharField(
                        choices=[
                            ("раз в день", "Ежедневно"),
                            ("раз в неделю", "Еженедельно"),
                            ("раз в месяц", "Ежемесячно"),
                        ],
                        max_length=300,
                        verbose_name="Частота отправки",
                    ),
                ),
                (
                    "status_of_newsletter",
                    models.CharField(
                        choices=[
                            ("Создана", "Создана"),
                            ("В работе", "В работе"),
                            ("Завершена", "Завершена"),
                            ("Ошибка отправки", "Ошибка отправки"),
                        ],
                        max_length=150,
                        verbose_name="статус рассылки",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="Активна"),
                ),
            ],
            options={
                "verbose_name": "Рассылка",
                "verbose_name_plural": "Рассылки",
                "permissions": [
                    ("can_view_all_newsletter", "Может видеть все рассылки"),
                    ("can_disable_newsletter", "Может отключать рассылки"),
                    ("cannot_change_newsletter", "Не может изменять рассылки"),
                    ("cannot_delete_newsletter", "Не может удалять рассылки"),
                    ("cannot_create_newsletter", "Не может создавать рассылки"),
                ],
            },
        ),
        migrations.CreateModel(
            name="TextForNewsletter",
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
                ("subject", models.CharField(max_length=200, verbose_name="тема")),
                ("text", models.TextField(verbose_name="текст")),
                (
                    "clients",
                    models.ManyToManyField(
                        blank=True,
                        to="schedule.client",
                        verbose_name="Клиенты для рассылки",
                    ),
                ),
            ],
            options={
                "verbose_name": "Текст для отправки",
                "verbose_name_plural": "Тексты для рассылок",
                "permissions": [
                    (
                        "cann_change_textfornewsletter_list",
                        "Может изменять текст для рассылок",
                    )
                ],
            },
        ),
    ]