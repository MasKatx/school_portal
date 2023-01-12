from django.urls import path
from .views import GetUsersView, GetUser

urlpatterns = [
    path("users", GetUsersView.as_view()),
    # path("user_profile", GetUser.as_view()),
]
