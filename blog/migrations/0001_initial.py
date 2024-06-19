from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Article",
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
                ("title", models.CharField(max_length=50, verbose_name="Заголовок")),
                ("body", models.TextField(verbose_name="Текст")),
                (
                    "preview",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="articles/",
                        verbose_name="Превью",
                    ),
                ),
                ("date", models.DateField(verbose_name="дата публикации")),
                (
                    "views_count",
                    models.PositiveIntegerField(default=0, verbose_name="просмотры"),
                ),
            ],
            options={
                "verbose_name": "статья",
                "verbose_name_plural": "статьи",
            },
        ),
    ]