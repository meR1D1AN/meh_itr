from django.utils import timezone
from django.contrib import messages

from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, View
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin

from lifts.forms import ReplacementForm, ProblemForm
from lifts.models import *


class ElevatorMixin:
    def get_elevator(self):
        elevator_id = self.kwargs.get("pk")
        return get_object_or_404(Elevator, pk=elevator_id)

    def get_building(self):
        elevator = self.get_elevator()
        return elevator.buildings.first()


class SuccessUrlMixin:
    def get_success_url(self):
        return reverse("lifts:elevator_detail", kwargs={"pk": self.kwargs["pk"]})


class BuildingListView(LoginRequiredMixin, ListView):
    model = Building


class BuildingDetailView(LoginRequiredMixin, DetailView):
    model = Building


class ElevatorListView(LoginRequiredMixin, ListView):
    model = Elevator


class ElevatorDetailView(LoginRequiredMixin, DetailView):
    model = Elevator

    def get_queryset(self):
        return Elevator.objects.all()

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        return self.object

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        elevator = self.get_object()
        context.update(
            {
                "problems": Problem.objects.filter(elevator=elevator).order_by("-id"),
                "replacements": Replacement.objects.filter(elevator=elevator).order_by(
                    "-id"
                ),
                "tos": TO.objects.filter(elevator=elevator).order_by("-date"),
            }
        )
        return context


class ProblemListView(LoginRequiredMixin, ListView):
    model = Problem


class ProblemCreateView(
    LoginRequiredMixin,
    ElevatorMixin,
    SuccessUrlMixin,
    CreateView,
):
    model = Problem
    form_class = ProblemForm

    def form_valid(self, form):
        form.instance.elevator = self.get_elevator()
        form.instance.buildings = self.get_building()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["buildings"] = self.get_building()
        context["elevator"] = self.get_elevator()
        return context


class ProblemResolveView(LoginRequiredMixin, View):
    def post(self, request, pk):
        problem = get_object_or_404(Problem, pk=pk)
        problem.resolved = True
        problem.save()
        return redirect(
            reverse("lifts:elevator_detail", kwargs={"pk": problem.elevator.pk})
        )


class ReplacementList(LoginRequiredMixin, ListView):
    model = Replacement


class ReplacementCreateView(
    LoginRequiredMixin,
    ElevatorMixin,
    SuccessUrlMixin,
    CreateView,
):
    model = Replacement
    form_class = ReplacementForm

    def form_valid(self, form):
        form.instance.elevator = self.get_elevator()
        form.instance.buildings = self.get_building()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["buildings"] = self.get_building()
        context["elevator"] = self.get_elevator()
        return context


class ReplacementResolveView(LoginRequiredMixin, View):
    def post(self, request, pk):
        replacement = get_object_or_404(Replacement, pk=pk)
        replacement.resolved = True
        replacement.save()
        return redirect(
            reverse("lifts:elevator_detail", kwargs={"pk": replacement.elevator.pk})
        )


class TOList(LoginRequiredMixin, ListView):
    model = TO


class TOCreateView(
    LoginRequiredMixin,
    ElevatorMixin,
    SuccessUrlMixin,
    CreateView,
):
    model = TO

    def form_valid(self, form):
        form.instance.elevator = self.get_elevator()
        form.instance.building = self.get_building()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["buildings"] = self.get_building()
        context["elevator"] = self.get_elevator()
        return context


class TOAutoCreateView(LoginRequiredMixin, ElevatorMixin, SuccessUrlMixin, View):
    def post(self, request, *args, **kwargs):
        # Получаем текущий лифт и здание
        elevator = self.get_elevator()
        building = self.get_building()

        # Проверяем, существует ли уже запись ТО для текущего лифта и сегодняшней даты
        today = timezone.now().date()
        if TO.objects.filter(elevator=elevator, date=today).exists():
            # Если запись уже существует, возвращаем сообщение или перенаправляем обратно
            messages.error(request, "Сегодняшняя запись ТО уже существует.")
            return redirect(self.get_success_url())

        # Создаём запись ТО с текущей датой
        TO.objects.create(elevator=elevator, building=building)

        # Перенаправляем обратно на детальную страницу лифта
        return redirect(self.get_success_url())


def home_view(request):
    if request.user.is_authenticated:
        # Если пользователь авторизован, перенаправляем его на страницу с лифтами
        return redirect("lifts:building_list")

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Если форма правильная, авторизуем пользователя и перенаправляем на /lifts/buildings/
            user = form.get_user()
            login(request, user)
            return redirect("lifts:building_list")
    else:
        form = AuthenticationForm()

    return render(request, "home.html", {"form": form})
