from django.urls import path
from .views import *
from lifts import apps

app_name = apps.LiftsConfig.name

urlpatterns = [
    path('buildings/', BuildingListView.as_view(), name='building_list'),
    path('buildings/<int:pk>/', BuildingDetailView.as_view(), name='building_detail'),
    path('buildings/create/', BuildingCreateView.as_view(), name='building_create'),
    path('elevators/', ElevatorListView.as_view(), name='elevator_list'),
    path('elevators/<int:pk>/', ElevatorDetailView.as_view(), name='elevator_detail'),
    path('problems/', ProblemList.as_view(), name='problem_list'),
    path('replacements/', ReplacementList.as_view(), name='replacement_list'),
    path('tos/', TOList.as_view(), name='to_list'),
]
