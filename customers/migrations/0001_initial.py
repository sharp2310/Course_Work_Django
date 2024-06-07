from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='e-mail')),
                ('description', models.TextField(blank=True, null=True, verbose_name='описание')),
                ('company_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='имя компании')),
            ],
            options={
                'verbose_name': 'клиент',
                'verbose_name_plural': 'клиенты',
            },
        ),
    ]