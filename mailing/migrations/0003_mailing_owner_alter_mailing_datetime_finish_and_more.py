import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mailing", "0002_log"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="mailing",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="автор",
            ),
        ),
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
    ]