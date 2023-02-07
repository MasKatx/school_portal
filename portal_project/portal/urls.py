from django.urls import path
from .views import (
    SchoolGroupView,
    CreateOrUpdateSchoolGroupView,
    DestroySchoolGroupView,
    # TestView,
    CreateorUpdatePostView,
    DeletePostView,
    ShowPostView,
    GetClassSchool,
    CreateClassSchool,
    UpdateClassSchool,
    DeleteClassSchool,
    GetPosterInfomationView,
    CreatePostView,
    UpdatePostView,
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
    path("create_post", CreatePostView.as_view()),
    path("get_userinfor_post/<int:post_num>", GetPosterInfomationView.as_view()),
    path("delete_post/<int:pk>", DeletePostView.as_view()),
    path("update_post/<int:pk>", UpdatePostView.as_view()),
    path("get_post/<int:post_num>", ShowPostView.as_view()),
    path("create/post", CreateorUpdatePostView.as_view()),
    path("delete_post/<int:pk>", DeletePostView.as_view()),
    path("update/<path:str>", CreateorUpdatePostView.as_view()),
    path("show/<path:str>", ShowPostView.as_view()),
    path("get_class", GetClassSchool.as_view()),
    path("create_class", CreateClassSchool.as_view()),
    path("update_class/<int:pk>", UpdateClassSchool.as_view()),
    path("delete_class/<int:pk>", DeleteClassSchool.as_view()),
]
