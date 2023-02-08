from django.urls import path
from .views import (
    SchoolGroupView,
    CreateOrUpdateSchoolGroupView,
    DestroySchoolGroupView,
    # TestView,
    CreateorUpdatePostView,
    ShowPostView,
    DeletePostView,
    GetClassSchool,
    CreateClassSchool,
    UpdateClassSchool,
    DeleteClassSchool,
    CreateChatView,
)


# GetUserProfileView,

urlpatterns = [
    path("group", SchoolGroupView.as_view()),
    path("create", CreateOrUpdateSchoolGroupView.as_view()),
    path("update/<int:pk>", CreateOrUpdateSchoolGroupView.as_view()),
    path(
        "delete_group/<int:pk>",
        DestroySchoolGroupView.as_view(),
    ),
    # path("test/<path:str>", TestView.as_view()),
    path("create/post", CreateorUpdatePostView.as_view()),
    path("update/<path:str>", CreateorUpdatePostView.as_view()),
    path("post/getpostview", ShowPostView.as_view()),
    path("delete/<path:str>", DeletePostView.as_view()),
    path("get_class", GetClassSchool.as_view()),
    path("create_class", CreateClassSchool.as_view()),
    path("update_class/<int:pk>", UpdateClassSchool.as_view()),
    path("delete_class/<int:pk>", DeleteClassSchool.as_view()),
    path("create/chat", CreateChatView.as_view()),
]
