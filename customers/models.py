from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Customer(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    email = models.EmailField(unique=True, verbose_name='e-mail')
    description = models.TextField(verbose_name='описание', **NULLABLE)

    company_name = models.CharField(max_length=50, verbose_name='имя компании', **NULLABLE)

    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, **NULLABLE, verbose_name='автор')

    def __str__(self):
        return f'{self.first_name} - {self.email}'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'