import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mailing", "0003_mailing_owner_alter_mailing_datetime_finish_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mailing",
            name="datetime_finish",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 6, 11, 16, 16, 21, 538),
                verbose_name="время окончания рассылки",
            ),
        ),
        migrations.AlterField(
            model_name="mailing",
            name="datetime_start",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 6, 11, 16, 16, 21, 538),
                verbose_name="время начала рассылки",
            ),
        ),
    ]