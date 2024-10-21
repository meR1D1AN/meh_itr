from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Employee
from .forms import EmployeeForm


class EmployeeListView(LoginRequiredMixin, ListView):
    model = Employee
    template_name = 'employee_list.html'
    context_object_name = 'employees'

    def get_queryset(self):
        # Если пользователь — администратор, показываем всех сотрудников
        if self.request.user.is_superuser:
            return Employee.objects.all()
        # Если обычный пользователь, показываем только тех, кого он сам создал
        return Employee.objects.filter(created_by=self.request.user)


class EmployeeCreateView(LoginRequiredMixin, CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'itr/employee_form.html'
    success_url = reverse_lazy('itr:employee_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  # Передаем текущего пользователя в форму
        return kwargs

    def form_valid(self, form):
        form.instance.created_by = self.request.user  # Автоматически назначаем создателя
        return super().form_valid(form)


class EmployeeDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Employee
    template_name = 'itr/employee_detail.html'
    context_object_name = 'employee'

    def test_func(self):
        employee = self.get_object()
        return self.request.user.is_superuser or self.request.user == employee.created_by
