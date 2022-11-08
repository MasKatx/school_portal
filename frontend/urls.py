from django.urls import path, include
from .views import index

urlpatterns = [
    path("home/", index),
    path("card/", index),
    path("library/", index),
    path("message/", index),
    path("studentsmanagement/", index),
    path("settings/", index),
    path("help/", index),
]
