from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    path("", include("accounts.urls")),
    path("profile/", include("user_profile.urls")),
]

urlpatterns += [
    re_path(r"^.*", TemplateView.as_view(template_name="index.html"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
