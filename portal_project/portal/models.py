from django.db import models
from django.conf import settings
import random
import string


def generate_unique_group_id():
    lenght = 12
    while True:
        group_id = "".join(random.choices(string.ascii_uppercase, k=lenght))
        if SchoolGroup.objects.filter(group_id=group_id).count() == 0:
            break
    return group_id


# Create your models here.
class SchoolGroup(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    group_name = models.CharField(max_length=255)
    group_phone = models.CharField(max_length=20)
    group_address = models.CharField(max_length=255)
    group_id = models.CharField(
        max_length=20, unique=True, default=generate_unique_group_id
    )
    created = models.DateTimeField(auto_now_add=True)
    sign = models.CharField(max_length=2, blank=True)
    bio = models.TextField(default="")

    def __str__(self):
        return self.group_id
