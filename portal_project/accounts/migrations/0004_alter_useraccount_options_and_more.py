# Generated by Django 4.1.3 on 2022-11-21 05:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_useraccount_can_do_anything_delete_userprofile"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="useraccount",
            options={"verbose_name": "user", "verbose_name_plural": "users"},
        ),
        migrations.RenameField(
            model_name="useraccount",
            old_name="name",
            new_name="username",
        ),
        migrations.RemoveField(
            model_name="useraccount",
            name="can_do_anything",
        ),
        migrations.AddField(
            model_name="useraccount",
            name="date_joined",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="date joined"
            ),
        ),
        migrations.AddField(
            model_name="useraccount",
            name="first_name",
            field=models.CharField(
                blank=True, max_length=150, verbose_name="first name"
            ),
        ),
        migrations.AddField(
            model_name="useraccount",
            name="last_name",
            field=models.CharField(
                blank=True, max_length=150, verbose_name="last name"
            ),
        ),
        migrations.AlterField(
            model_name="useraccount",
            name="is_superuser",
            field=models.BooleanField(default=True),
        ),
    ]
