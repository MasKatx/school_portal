from django.db import models
from django.conf import settings


def upload_path(instance, filname):
    return "/".join(["covers", str(instance.group_name), filname])


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=255, default="", blank=True)
    phone = models.CharField(max_length=20, default="", blank=True)
    address = models.CharField(max_length=255, default="", blank=True)
    avatar = models.ImageField(upload_to=upload_path, blank=True)
    date_of_birth = models.DateField(help_text="The date of birth", blank=True)
    user_types = [
        ("1", "admin"),
        ("2", "teacher"),
        ("3", "student"),
    ]
    group_name = models.CharField(max_length=255, default="", blank=True)
    user_type = models.CharField(
        max_length=255, choices=user_types, default="1", blank=True
    )
    teacher_library = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.fullname
