from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_user_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="id",
            field=models.IntegerField(
                editable=False,
                primary_key=True,
                serialize=False,
                verbose_name="id_клиента",
            ),
        ),
    ]