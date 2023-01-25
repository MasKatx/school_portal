# import from django
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

# others
import string
import random


def upload_path(instance, filname):
    return "/".join(["covers", str(instance.user.username), filname])


class UserAvatar(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=upload_path, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = "user_avatar"


# admin profile
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=255, blank=True)
    date_of_birth = models.DateField(
        help_text="The date of birth", blank=True, null=True
    )
    teacher_library = models.BooleanField(default=False, blank=True)
    user_types = [
        ("1", "admin"),
        ("2", "teacher"),
        ("3", "student"),
    ]
    user_type = models.CharField(max_length=255, choices=user_types, default="1")
    # teacher profile
    teacher_sexs = [
        ("1", "male"),
        ("2", "female"),
        ("3", "others"),
    ]
    teacher_sex = models.CharField(max_length=255, choices=teacher_sexs, default="1")
    teacher_belong_to_id = models.CharField(max_length=255, blank=True)
    teacher_belong_to_name = models.CharField(max_length=255, blank=True)
    teacher_course = models.CharField(max_length=255, blank=True)
    # 学生情報
    student_id = models.CharField(max_length=30, blank=True)
    school_id = models.CharField(max_length=255, blank=True)
    student_class_name = models.CharField(max_length=5, blank=True)
    student_fullname_furigana = models.CharField(max_length=255, blank=True)
    student_post_num = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = "user_profile"


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        UserAvatar.objects.create(user=instance)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    instance.useravatar.save()
    instance.userprofile.save()
