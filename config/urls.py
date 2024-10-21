from django.contrib import admin
from django.urls import path, include

from lifts.views import home_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("lifts/", include("lifts.urls"), name="lifts"),
    path("", home_view, name="home"),  # Путь для главной страницы
    path("itr/", include("itr.urls"), name="itr"),
]
