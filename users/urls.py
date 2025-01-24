from django.urls import path
from users import apps
from users.views import change_password_view, edit_profile, profile

app_name = apps.UsersConfig.name

urlpatterns = [
    path("profile/", profile, name="profile"),
    path("profile/edit/", edit_profile, name="edit_profile"),
    path("change_password/", change_password_view, name="change_password"),
]
