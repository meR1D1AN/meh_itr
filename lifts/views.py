from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin

from lifts.forms import TOForm
from lifts.models import *


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
        context['problems'] = Problem.objects.filter(elevator=elevator, resolved=False)
        context['replacements'] = Replacement.objects.filter(elevator=elevator, resolved=False)
        context['tos'] = TO.objects.filter(elevator=elevator)
        return context


class ProblemListView(LoginRequiredMixin, ListView):
    model = Problem


class ProblemCreateView(LoginRequiredMixin, CreateView):
    model = Problem
    fields = ["problem"]

    def form_valid(self, form):
        elevator_id = self.kwargs['pk']
        elevator = Elevator.objects.get(pk=elevator_id)

        try:
            building = elevator.buildings.first()  # Получаем первое здание, в котором находится лифт
        except ObjectDoesNotExist:
            building = None  # Если здание не найдено, устанавливаем building в None

        form.instance.elevator_id = elevator_id
        if building:
            form.instance.buildings = building  # Устанавливаем здание в форму, если оно найдено

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('lifts:elevator_detail', kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        elevator_id = self.kwargs['pk']
        elevator = Elevator.objects.get(pk=elevator_id)

        try:
            context['buildings'] = elevator.buildings.first()
        except ObjectDoesNotExist:
            context['buildings'] = None

        context['elevator'] = elevator  # Добавляем elevator в контекст
        return context


class ProblemResolveView(LoginRequiredMixin, View):
    def post(self, request, pk):
        problem = get_object_or_404(Problem, pk=pk)
        problem.resolved = True
        problem.save()
        return redirect(reverse('lifts:elevator_detail', kwargs={'pk': problem.elevator.pk}))


class ReplacementList(LoginRequiredMixin, ListView):
    model = Replacement


class ReplacementCreateView(LoginRequiredMixin, CreateView):
    model = Replacement
    fields = ["info_problem"]

    def form_valid(self, form):
        elevator_id = self.kwargs['pk']
        elevator = Elevator.objects.get(pk=elevator_id)

        try:
            building = elevator.buildings.first()  # Получаем первое здание, в котором находится лифт
        except ObjectDoesNotExist:
            building = None  # Если здание не найдено, устанавливаем building в None

        form.instance.elevator_id = elevator_id
        if building:
            form.instance.buildings = building  # Устанавливаем здание в форму, если оно найдено

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('lifts:elevator_detail', kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        elevator_id = self.kwargs['pk']
        elevator = Elevator.objects.get(pk=elevator_id)

        try:
            context['buildings'] = elevator.buildings.first()
        except ObjectDoesNotExist:
            context['buildings'] = None

        context['elevator'] = elevator  # Добавляем elevator в контекст
        return context


class ReplacementResolveView(LoginRequiredMixin, View):
    def post(self, request, pk):
        replacement = get_object_or_404(Replacement, pk=pk)
        replacement.resolved = True
        replacement.save()
        return redirect(reverse('lifts:elevator_detail', kwargs={'pk': replacement.elevator.pk}))


class TOList(LoginRequiredMixin, ListView):
    model = TO


class TOCreateView(LoginRequiredMixin, CreateView):
    model = TO
    form_class = TOForm

    def form_valid(self, form):
        elevator_id = self.kwargs['pk']
        elevator = Elevator.objects.get(pk=elevator_id)

        try:
            building = elevator.buildings.first()  # Получаем первое здание, в котором находится лифт
        except ObjectDoesNotExist:
            building = None  # Если здание не найдено, устанавливаем building в None

        form.instance.elevator_id = elevator_id
        if building:
            form.instance.building = building  # Устанавливаем здание в форму, если оно найдено

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('lifts:elevator_detail', kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        elevator_id = self.kwargs['pk']
        elevator = Elevator.objects.get(pk=elevator_id)

        try:
            context['buildings'] = elevator.buildings.first()
        except ObjectDoesNotExist:
            context['buildings'] = None

        context['elevator'] = elevator  # Добавляем elevator в контекст
        return context


def home_view(request):
    if request.user.is_authenticated:
        # Если пользователь авторизован, перенаправляем его на страницу с лифтами
        return redirect('lifts:building_list')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Если форма правильная, авторизуем пользователя и перенаправляем на /lifts/buildings/
            user = form.get_user()
            login(request, user)
            return redirect('lifts:building_list')
    else:
        form = AuthenticationForm()

    return render(request, 'home.html', {'form': form})
