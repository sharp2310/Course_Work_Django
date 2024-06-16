from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_alter_user_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="id",
            field=models.IntegerField(
                default=3,
                primary_key=True,
                serialize=False,
                verbose_name="id_пользователя",
            ),
        ),
    ]