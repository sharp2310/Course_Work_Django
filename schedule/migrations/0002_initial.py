from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("schedule", "0001_initial"),
        ("users", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="textfornewsletter",
            name="company",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="users.company",
                verbose_name="Компания",
            ),
        ),
        migrations.AddField(
            model_name="newsletter",
            name="clients",
            field=models.ManyToManyField(to="schedule.client", verbose_name="Клиенты"),
        ),
        migrations.AddField(
            model_name="newsletter",
            name="message",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="schedule.textfornewsletter",
                verbose_name="Сообщение для отправки",
            ),
        ),
        migrations.AddField(
            model_name="newsletter",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Владелец",
            ),
        ),
        migrations.AddField(
            model_name="log",
            name="client",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="schedule.client",
                verbose_name="Клиент",
            ),
        ),
        migrations.AddField(
            model_name="log",
            name="company",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="users.company",
                verbose_name="Компания",
            ),
        ),
        migrations.AddField(
            model_name="log",
            name="mailing_list",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="schedule.newsletter",
                verbose_name="Рассылка",
            ),
        ),
        migrations.AddField(
            model_name="log",
            name="message",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="schedule.textfornewsletter",
                verbose_name="Сообщение",
            ),
        ),
        migrations.AddField(
            model_name="client",
            name="company",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="users.company",
                verbose_name="Компания",
            ),
        ),
    ]