from django.urls import path
from .views import (
    GetUsersView,
    GetUser,
    UpdateUserAccountPassword,
)

urlpatterns = [
    path("users", GetUsersView.as_view()),
    path("change_password", UpdateUserAccountPassword.as_view()),
    # path("user_profile", GetUser.as_view()),
]
