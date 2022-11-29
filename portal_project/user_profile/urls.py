from django.urls import path
from .views import UpdateUserProfileView, GetUserProfileView

# GetUserProfileView,

urlpatterns = [
    path("user/", GetUserProfileView.as_view()),
    path("update", UpdateUserProfileView.as_view()),
]
