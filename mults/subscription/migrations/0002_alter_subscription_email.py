# Generated by Django 4.1.4 on 2022-12-30 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("subscription", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="subscription",
            name="email",
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
