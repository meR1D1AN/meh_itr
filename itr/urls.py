from django.urls import path
from .views import *
from itr import apps
from . import views

app_name = apps.ItrConfig.name

urlpatterns = [
    path("employees/", EmployeeListView.as_view(), name="employee_list"),
    path("employees/create/", EmployeeCreateView.as_view(), name="employee_create"),
    path("employees/<int:pk>/", EmployeeDetailView.as_view(), name="employee_detail"),
    path(
        "employees/<int:pk>/update/",
        EmployeeUpdateView.as_view(),
        name="employee_update",
    ),
    path("customers/", CustomerListView.as_view(), name="customer_list"),
    path("customers/create/", CustomerCreateView.as_view(), name="customer_create"),
    path("customers/<int:pk>/", CustomerDetailView.as_view(), name="customer_detail"),
    path(
        "customers/<int:pk>/update/",
        CustomerUpdateView.as_view(),
        name="customer_update",
    ),
    path("search/", views.search_view, name="search"),
    path(
        "customers/<int:pk>/calculate_salary/",
        views.calculate_salary,
        name="calculate_salary",
    ),
    path(
        "customers/<int:pk>/excel/", CustomerExcelView.as_view(), name="customer_excel"
    ),
    path("vacations/", VacationListView.as_view(), name="vacation_list"),
    path("vacations/create/", VacationCreateView.as_view(), name="vacation_create"),
    path(
        "vacations/<int:pk>/update/",
        VacationUpdateView.as_view(),
        name="vacation_update",
    ),
    path("vacations/<int:pk>/", VacationDetailView.as_view(), name="vacation_detail"),
    path(
        "vacations/<int:pk>/approve/",
        VacationApproveView.as_view(),
        name="vacation_approve",
    ),
]
