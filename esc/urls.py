from django.urls import path
from .views import *
from esc import apps

app_name = apps.EscConfig.name

urlpatterns = [
    # Эскалаторы
    path("escalators/", EscListView.as_view(), name="escalator_list"),
    path("escalators/<int:pk>/", EscDetailView.as_view(), name="escalator_detail"),
    path(
        "escalators/<int:pk>/to/auto-create/",
        EscTOAutoCreateView.as_view(),
        name="to_auto_create",
    ),
    # Проблемы
    path("problems/", EscProblemListView.as_view(), name="problem_list"),
    path(
        "problems/create/<int:pk>/", EscProblemCreateView.as_view(), name="problem_form"
    ),
    path(
        "problems/<int:pk>/resolve/",
        EscProblemResolveView.as_view(),
        name="problem_resolve",
    ),
    # Ремонты
    path("replaces/", EscReplaceList.as_view(), name="replace_list"),
    path(
        "replaces/create/<int:pk>/", EscReplaceCreateView.as_view(), name="replace_form"
    ),
    path(
        "replaces/<int:pk>/resolve/",
        EscReplaceResolveView.as_view(),
        name="replace_resolve",
    ),
    # ТО
    path("tos/", EscTOList.as_view(), name="to_list"),
]
