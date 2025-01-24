from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from lifts.views import home_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("lifts/", include("lifts.urls"), name="lifts"),
    path("", home_view, name="home"),  # Путь для главной страницы
    path("itr/", include("itr.urls"), name="itr"),
    path("esc/", include("esc.urls"), name="esc"),
    path("users/", include("users.urls"), name="users"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
