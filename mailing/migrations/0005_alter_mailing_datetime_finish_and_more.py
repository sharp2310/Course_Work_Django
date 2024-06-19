import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mail_messages", "0003_alter_message_owner"),
        ("mailing", "0004_alter_mailing_datetime_finish_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mailing",
            name="datetime_finish",
            field=models.DateTimeField(verbose_name="время окончания рассылки"),
        ),
        migrations.AlterField(
            model_name="mailing",
            name="datetime_start",
            field=models.DateTimeField(verbose_name="время начала рассылки"),
        ),
        migrations.AlterField(
            model_name="mailing",
            name="messages",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="mail_messages.message",
                verbose_name="Сообщение",
            ),
        ),
        migrations.AlterField(
            model_name="mailing",
            name="period",
            field=models.CharField(
                choices=[
                    ("Единоразовая", "Единоразовая"),
                    ("Раз в день", "Раз в день"),
                    ("Раз в неделю", "Раз в неделю"),
                    ("Раз в месяц", "Раз в месяц"),
                ],
                default="Раз в день",
                max_length=25,
                verbose_name="периодичность",
            ),
        ),
        migrations.AlterField(
            model_name="mailing",
            name="status",
            field=models.CharField(
                choices=[
                    ("created", "Создана"),
                    ("started", "Запущена"),
                    ("finished", "Завершена"),
                ],
                default="created",
                max_length=25,
                verbose_name="статус",
            ),
        ),
    ]