from django.urls import path
from .views import (
    SchoolGroupView,
    CreateOrUpdateSchoolGroupView,
    DestroySchoolGroupView,
    # TestView,
    CreateOrUpdateClassGroupView,
    CreateorUpdatePostView,
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
    path("create/create_class", CreateOrUpdateClassGroupView.as_view()),
    path("create/post", CreateorUpdatePostView.as_view()),
]
