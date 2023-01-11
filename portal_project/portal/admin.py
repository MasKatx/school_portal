from django.contrib import admin

# Register your models here.
from .models import SchoolGroup, GroupInfomation

admin.site.register(SchoolGroup)
admin.site.register(GroupInfomation)
