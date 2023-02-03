from django.contrib import admin

# Register your models here.
from .models import (
    SchoolGroup,
    ClassGroup,
    PostModels,
    ChatSpace,
)  # , ChatRoom, ChatValue

admin.site.register(SchoolGroup)

admin.site.register(ClassGroup)

admin.site.register(PostModels)

admin.site.register(ChatSpace)

# admin.site.register(ChatRoom)

# admin.site.register(ChatValue)
