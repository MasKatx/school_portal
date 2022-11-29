from django.urls import path
from .views import GetUsersView

urlpatterns = [
    path("users/", GetUsersView.as_view()),
]
