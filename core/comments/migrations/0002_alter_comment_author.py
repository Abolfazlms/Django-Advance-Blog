# Generated by Django 3.2.25 on 2024-10-08 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_user_is_verified"),
        ("comments", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="accounts.profile"
            ),
        ),
    ]
