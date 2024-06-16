from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_alter_user_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="id",
            field=models.IntegerField(
                default=3,
                editable=False,
                primary_key=True,
                serialize=False,
                verbose_name="id_пользователя",
            ),
        ),
    ]