from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from lifts.models import *


class BuildingListView(ListView):
    model = Building


class BuildingDetailView(DetailView):
    model = Building


class BuildingCreateView(CreateView):
    model = Building
    fields = "__all__"

    def get_success_url(self):
        return reverse_lazy("lifts:building_list")


class ElevatorListView(ListView):
    model = Elevator


class ElevatorDetailView(DetailView):
    model = Elevator

    def get_queryset(self):
        return Elevator.objects.all()

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        return self.object

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        elevator = self.get_object()
        context['problems'] = Problem.objects.filter(elevator=elevator, resolved=False)
        context['replacements'] = Replacement.objects.filter(elevator=elevator, resolved=False)
        context['tos'] = TO.objects.filter(elevator=elevator)
        return context


class ProblemList(ListView):
    model = Problem
    template_name = "lifts/problem_list.html"
    context_object_name = "problems"


class ReplacementList(ListView):
    model = Replacement
    template_name = "lifts/replacement_list.html"
    context_object_name = "replacements"


class TOList(ListView):
    model = TO
    template_name = "lifts/to_list.html"
    context_object_name = "tos"
