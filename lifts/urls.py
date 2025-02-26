from django.contrib.auth import views as auth_views
from django.urls import path

from lifts import apps

from .views import (
    BuildingDetailView,
    BuildingListView,
    ElevatorDetailView,
    ElevatorListView,
    ProblemCreateView,
    ProblemListView,
    ProblemResolveView,
    ReplacementCreateView,
    ReplacementList,
    ReplacementResolveView,
    TOAutoCreateView,
    TOCreateView,
    TOList,
)


app_name = apps.LiftsConfig.name

urlpatterns = [
    # ЗДАНИЕ
    path("buildings/", BuildingListView.as_view(), name="building_list"),
    path("buildings/<int:pk>/", BuildingDetailView.as_view(), name="building_detail"),
    # ЛИФТЫ
    path("elevators/", ElevatorListView.as_view(), name="elevator_list"),
    path("elevators/<int:pk>/", ElevatorDetailView.as_view(), name="elevator_detail"),
    path("elevators/<int:pk>/to/auto-create/", TOAutoCreateView.as_view(), name="to_auto_create"),
    # ПРОБЛЕМЫ
    path("problems/", ProblemListView.as_view(), name="problem_list"),
    path("problems/create/<int:pk>/", ProblemCreateView.as_view(), name="problem_form"),
    path("problems/<int:pk>/resolve/", ProblemResolveView.as_view(), name="problem_resolve"),
    # РЕМОНТЫ
    path("replacements/", ReplacementList.as_view(), name="replacement_list"),
    path("replacements/create/<int:pk>/", ReplacementCreateView.as_view(), name="replacement_form"),
    path("replacements/<int:pk>/resolve/", ReplacementResolveView.as_view(), name="replacement_resolve"),
    # ТО
    path("tos/", TOList.as_view(), name="to_list"),
    path("tos/create/<int:pk>/", TOCreateView.as_view(), name="to_form"),
    # ВЫХОД
    path(
        "logout/", auth_views.LogoutView.as_view(), name="logout"
    ),  # Убедитесь, что имя 'logout' правильно определено
]
