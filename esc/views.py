from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils import timezone
from django.views import View
from django.views.generic import ListView, DetailView, CreateView

from esc.forms import EscProblemForm, EscReplaceForm
from esc.models import Esc, EscProblem, EscReplace, EscTO


class EscMixin:
    def get_esc(self):
        esc_id = self.kwargs.get("pk")
        return get_object_or_404(Esc, pk=esc_id)


class SuccessUrlMixin:
    def get_success_url(self):
        return reverse("esc:escalator_detail", kwargs={"pk": self.kwargs["pk"]})


class EscListView(LoginRequiredMixin, ListView):
    model = Esc

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object_list = self.get_queryset()
        grouped_escalators = {}

        for esc in object_list:
            prefix = esc.esc[:2]  # Получаем префикс, например "E1"
            if prefix not in grouped_escalators:
                grouped_escalators[prefix] = []
            grouped_escalators[prefix].append(esc)

        context["object_list"] = grouped_escalators

        # Добавляем все проблемы
        context["problems"] = EscProblem.objects.filter(resolved=False).order_by('-create_at')

        return context


class EscDetailView(LoginRequiredMixin, EscMixin, SuccessUrlMixin, DetailView):
    model = Esc

    def get_queryset(self):
        return Esc.objects.all()

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        return self.object

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        esc = self.get_object()
        context.update(
            {
                "problems": EscProblem.objects.filter(esc=esc).order_by("-id"),
                "replaces": EscReplace.objects.filter(esc=esc).order_by("-id"),
                "tos": EscTO.objects.filter(esc=esc).order_by("-create_at"),
            }
        )
        return context


class EscProblemListView(LoginRequiredMixin, ListView):
    model = EscProblem


class EscProblemCreateView(LoginRequiredMixin, EscMixin, SuccessUrlMixin, CreateView):
    model = EscProblem
    form_class = EscProblemForm

    def form_valid(self, form):
        form.instance.esc = self.get_esc()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["esc"] = self.get_esc()
        return context


class EscProblemResolveView(LoginRequiredMixin, View):
    def post(self, request, pk):
        problem = get_object_or_404(EscProblem, pk=pk)
        problem.resolved = True
        problem.save()
        return redirect(reverse("esc:escalator_detail", kwargs={"pk": problem.esc.pk}))


class EscReplaceList(LoginRequiredMixin, ListView):
    model = EscReplace


class EscReplaceCreateView(LoginRequiredMixin, EscMixin, SuccessUrlMixin, CreateView):
    model = EscReplace
    form_class = EscReplaceForm

    def form_valid(self, form):
        form.instance.esc = self.get_esc()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["esc"] = self.get_esc()
        return context


class EscReplaceResolveView(LoginRequiredMixin, View):
    def post(self, request, pk):
        replace = get_object_or_404(EscReplace, pk=pk)
        replace.resolved = True
        replace.save()
        return redirect(reverse("esc:escalator_detail", kwargs={"pk": replace.esc.pk}))


class EscTOList(LoginRequiredMixin, ListView):
    model = EscTO


class EscTOAutoCreateView(LoginRequiredMixin, EscMixin, SuccessUrlMixin, View):

    def post(self, request, *args, **kwargs):
        esc = self.get_esc()

        today = timezone.now().date()
        if EscTO.objects.filter(esc=esc, create_at__date=today).exists():
            messages.error(request, "Сегодняшняя запись ТО уже существует.")
            return redirect(self.get_success_url())

        EscTO.objects.create(esc=esc)
        return redirect(self.get_success_url())
