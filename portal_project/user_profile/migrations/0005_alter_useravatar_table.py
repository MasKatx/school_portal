# Generated by Django 4.1.3 on 2023-01-11 05:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user_profile", "0004_alter_userprofile_date_of_birth_and_more"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="useravatar",
            table="user_avatar",
        ),
    ]