# Generated by Django 5.0.1 on 2024-02-18 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="email",
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name="profile",
            name="first_name",
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name="profile",
            name="last_name",
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name="profile",
            name="bio",
            field=models.TextField(null=True),
        ),
    ]
