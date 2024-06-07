import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
        ('mail_messages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_start', models.DateTimeField(auto_now_add=True, verbose_name='время начала рассылки')),
                ('datetime_finish', models.DateTimeField(auto_now=True, verbose_name='время окончания рассылки')),
                ('period', models.CharField(choices=[('ONCE', 'Единоразовая'), ('DAILY', 'Раз в день'), ('WEEKLY', 'Раз в неделю'), ('MONTHLY', 'Раз в месяц')], default='DAILY', max_length=25, verbose_name='периодичность')),
                ('status', models.CharField(choices=[('CREATED', 'Создана'), ('STARTED', 'Запущена'), ('FINISHED', 'Завершена')], default='CREATED', max_length=25, verbose_name='периодичность')),
                ('customers', models.ManyToManyField(to='customers.customer', verbose_name='Контакты клиентов')),
                ('messages', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mail_messages.message', verbose_name='Сообщение')),
            ],
            options={
                'verbose_name': 'рассылка',
                'verbose_name_plural': 'рассылки',
            },
        ),
    ]