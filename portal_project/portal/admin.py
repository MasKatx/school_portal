from django.contrib import admin

# Register your models here.
from .models import SchoolGroup, ClassGroup, PostModels

admin.site.register(SchoolGroup)

admin.site.register(ClassGroup)

admin.site.register(PostModels)
