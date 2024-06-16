from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="id",
            field=models.IntegerField(
                default=2,
                editable=False,
                primary_key=True,
                serialize=False,
                verbose_name="id_клиента",
            ),
        ),
    ]