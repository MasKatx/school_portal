from django.db import models
from django.conf import settings


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, default="")
    last_name = models.CharField(max_length=255, default="")
    phone = models.CharField(max_length=20, default="")
    address = models.CharField(max_length=255, default="")
    avatar = models.ImageField(upload_to="pictures")

    def __str__(self):
        return self.first_name
