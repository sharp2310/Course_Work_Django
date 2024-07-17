from django.db import models

from users.models import Company, User

CREATE = "Создана"
IN_WORK = "В работе"
DONE = "Завершена"
ERROR = "Ошибка отправки"

DAILY = "раз в день"
WEEKLY = "раз в неделю"
MONTHLY = "раз в месяц"

FREQUENCY_CHOICES = [
    (DAILY, "Ежедневно"),
    (WEEKLY, "Еженедельно"),
    (MONTHLY, "Ежемесячно"),
]
STATUS_OF_NEWSLETTER = [
    (CREATE, "Создана"),
    (IN_WORK, "В работе"),
    (DONE, "Завершена"),
    (ERROR, "Ошибка отправки"),
]


class Client(models.Model):
    contact_email = models.EmailField(
        max_length=50, verbose_name="Email", help_text="Введите свой email", unique=True
    )
    fullname = models.TextField(verbose_name="фио")
    comment = models.CharField(max_length=250, verbose_name="комментарий")
    company = models.ForeignKey(
        Company,
        on_delete=models.SET_NULL,
        verbose_name="Компания",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.contact_email} {self.fullname} {self.comment}"

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"


class TextForNewsletter(models.Model):
    subject = models.CharField(max_length=200, verbose_name="тема")
    text = models.TextField(verbose_name="текст")
    clients = models.ManyToManyField(
        Client, verbose_name="Клиенты для рассылки", blank=True
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.SET_NULL,
        verbose_name="Компания",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.subject} {self.text}"

    class Meta:
        verbose_name = "Текст для отправки"
        verbose_name_plural = "Тексты для рассылок"
        permissions = [
            (
                "cann_change_textfornewsletter_list",
                "Может изменять текст для рассылок",
            ),
        ]


class Newsletter(models.Model):
    start_time = models.DateTimeField(
        verbose_name="время начала рассылки", blank=True, null=True
    )
    end_time = models.DateTimeField(
        verbose_name="время окончания рассылки", blank=True, null=True
    )
    frequency = models.CharField(
        max_length=300, choices=FREQUENCY_CHOICES, verbose_name="Частота отправки"
    )
    status_of_newsletter = models.CharField(
        max_length=150, verbose_name="статус рассылки", choices=STATUS_OF_NEWSLETTER
    )
    is_active = models.BooleanField(default=True, verbose_name="Активна")
    clients = models.ManyToManyField(Client, verbose_name="Клиенты")
    message = models.ForeignKey(
        TextForNewsletter,
        verbose_name="Сообщение для отправки",
        on_delete=models.CASCADE,
    )
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Владелец", null=True, blank=True
    )

    def __str__(self):
        return f"{self.start_time} {self.end_time} {self.frequency} {self.status_of_newsletter} {self.clients} {self.message}"

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"

        permissions = [
            ("can_view_all_newsletter", "Может видеть все рассылки"),
            ("can_disable_newsletter", "Может отключать рассылки"),
            ("cannot_change_newsletter", "Не может изменять рассылки"),
            ("cannot_delete_newsletter", "Не может удалять рассылки"),
            ("cannot_create_newsletter", "Не может создавать рассылки"),
        ]


class Log(models.Model):
    time_attempt = models.DateTimeField(
        verbose_name="дата и время последней попытки",
        auto_now_add=True,
        null=True,
        blank=True,
    )
    status_of_last_attempt = models.BooleanField(
        verbose_name="Статус попытки", null=True, blank=True
    )
    client = models.ForeignKey(
        Client, verbose_name="Клиент", on_delete=models.CASCADE, null=True, blank=True
    )
    message = models.ForeignKey(
        TextForNewsletter,
        verbose_name="Сообщение",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    mailing_list = models.ForeignKey(
        Newsletter,
        verbose_name="Рассылка",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    server_response = models.CharField(
        verbose_name="Ответ почтового сервера", max_length=255, null=True, blank=True
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.SET_NULL,
        verbose_name="Компания",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"Попытка отправки для {self.client} по рассылке {self.mailing_list}"

    class Meta:
        verbose_name = "Лог отправки сообщения"
        verbose_name_plural = "Логи отправки сообщений"