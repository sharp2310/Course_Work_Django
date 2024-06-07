from django.db import models

from customers.models import Customer
from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Mailing(models.Model):
    #  варианты периодичности рассылки
    ONCE = 'Единоразовая'
    DAILY = 'Раз в день'
    WEEKLY = 'Раз в неделю'
    MONTHLY = 'Раз в месяц'

    PERIOD_CHOICES = (
        ('ONCE', 'Единоразовая'),
        ('DAILY', 'Раз в день'),
        ('WEEKLY', 'Раз в неделю'),
        ('MONTHLY', 'Раз в месяц'),
    )
    #  варианты статуса рассылки
    CREATED = 'created'
    STARTED = 'started'
    FINISHED = 'finished'

    STATUS_CHOICES = (
        ('CREATED', 'Создана'),
        ('STARTED', 'Запущена'),
        ('FINISHED', 'Завершена'),
    )

    datetime_start = models.DateTimeField(auto_now_add=True, verbose_name='время начала рассылки')
    datetime_finish = models.DateTimeField(auto_now=True, verbose_name='время окончания рассылки')
    period = models.CharField(max_length=25, choices=PERIOD_CHOICES, default='DAILY', verbose_name='периодичность')
    status = models.CharField(max_length=25, choices=STATUS_CHOICES, default='CREATED', verbose_name='периодичность')

    customers = models.ManyToManyField('customers.Customer', verbose_name='Контакты клиентов')
    messages = models.ForeignKey('mail_messages.Message', on_delete=models.CASCADE, verbose_name='Сообщение')

    owner = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE, verbose_name='автор')

    def __str__(self):
        return f'{self.datetime_start}-{self.datetime_finish}, {self.period}, {self.status}'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'


class Log(models.Model):
    """Логи рассылки"""
    SUCCESS = 'success'
    FAIL = 'fail'

    STATUSES = (
        (SUCCESS, 'успешно'),
        (FAIL, 'не успешно')
    )
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='рассылка')
    clients = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True, verbose_name='контакты клиентов')
    try_time = models.DateTimeField(auto_now_add=True, verbose_name='дата и время последней попытки')
    try_status = models.CharField(max_length=50, choices=STATUSES, verbose_name='статус попытки')
    server_answer = models.CharField(max_length=250, null=True, blank=True, verbose_name='ответ почтового сервера')

    def __str__(self):
        return f'{self.try_time}: {self.try_status}'

    class Meta:
        verbose_name = 'лог'
        verbose_name_plural = 'логи'