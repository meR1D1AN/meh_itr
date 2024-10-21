from django.urls import path
from .views import EmployeeListView, EmployeeCreateView, EmployeeDetailView
from itr import apps


app_name = apps.ItrConfig.name

urlpatterns = [
    path('employees/', EmployeeListView.as_view(), name='employee_list'),
    path('employees/create/', EmployeeCreateView.as_view(), name='employee_create'),
    path('employees/<int:pk>/', EmployeeDetailView.as_view(), name='employee_detail'),
]
