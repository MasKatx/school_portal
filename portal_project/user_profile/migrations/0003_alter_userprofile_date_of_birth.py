# Generated by Django 4.1.3 on 2023-01-11 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user_profile", "0002_alter_userprofile_date_of_birth"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="date_of_birth",
            field=models.DateField(blank=True, help_text="The date of birth"),
        ),
    ]