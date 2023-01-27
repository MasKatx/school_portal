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


# クラスグループ
class ClassGroup(models.Model):
    school_group = models.ForeignKey(SchoolGroup, on_delete=models.CASCADE)
    class_name = models.CharField(max_length=255)
    class_studentnumber = models.IntegerField(blank=True)
    class_course = models.CharField(max_length=255)
    class_manager = models.CharField(max_length=255)
    class_submanager = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.class_name


# 掲示板のmodelsを作成する
# そのあとadminにうねうねする
# その次にviewsにAPI接続できるように頑張る
# 掲示板
class PostModels(models.Model):
    user = models.ForeignKey(SchoolGroup, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    created_by_id = models.CharField(max_length=255)

    def __str__(self):
        return self.title
