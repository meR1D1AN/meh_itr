from django import forms
from django.core.exceptions import ValidationError
from django.db.models import Q

from .models import Employee, Customer, WorkDay, Vacation
from users.models import User


class EmployeeForm(forms.ModelForm):
    # Используем DateInput с форматом YYYY-MM-DD
    date_registration = forms.DateField(
        widget=forms.DateInput(
            attrs={"type": "date", "class": "form-control"}, format="%Y-%m-%d"
        ),
        label="Дата регистрации",
        required=True,
    )
    date_of_birth = forms.DateField(
        widget=forms.DateInput(
            attrs={"type": "date", "class": "form-control"}, format="%Y-%m-%d"
        ),
        label="Дата рождения",
        required=True,
    )
    hire_date = forms.DateField(
        widget=forms.DateInput(
            attrs={"type": "date", "class": "form-control"}, format="%Y-%m-%d"
        ),
        label="Дата приема на работу",
        required=True,
    )
    issued_when = forms.DateField(
        widget=forms.DateInput(
            attrs={"type": "date", "class": "form-control"}, format="%Y-%m-%d"
        ),
        label="Дата выдачи паспорта",
        required=True,
    )
    date_of_termination = forms.DateField(
        widget=forms.DateInput(
            attrs={"type": "date", "class": "form-control"}, format="%Y-%m-%d"
        ),
        label="Дата увольнения",
        required=False,
    )
    customer = forms.ModelMultipleChoiceField(
        queryset=Customer.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={"class": "form-control"}),
        label="Выберите или создайте нового",
        required=False,
    )

    class Meta:
        model = Employee
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)  # Получаем текущего пользователя
        super(EmployeeForm, self).__init__(*args, **kwargs)

        # Устанавливаем queryset и label для поля created_by
        self.fields["created_by"].queryset = User.objects.all()
        self.fields["created_by"].label_from_instance = (
            lambda obj: f"{obj.last_name} {obj.first_name[0]}."
        )

        # Если пользователь не администратор, скрываем поле "created_by"
        if not user.is_superuser:
            self.fields["created_by"].widget = forms.HiddenInput()


class CustomerForm(forms.ModelForm):
    start_work = forms.DateField(
        widget=forms.DateInput(
            attrs={"type": "date", "class": "form-control"}, format="%Y-%m-%d"
        ),
        label="Дата начала работы",
        help_text="Укажите дату начала работы по графику 1/3",
        required=False,
    )

    class Meta:
        model = Customer
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Правильный вызов super()

        self.fields["created_by"].queryset = User.objects.all()
        self.fields["created_by"].label_from_instance = (
            lambda obj: f"{obj.last_name} {obj.first_name[0]}."
        )
        self.fields["work_schedule"].widget.attrs.update({"class": "work-schedule"})
        self.fields["start_work"].widget.attrs.update({"class": "start-work"})


class CombinedEmployeeCustomerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)

        # Инициализация полей Employee
        employee_form = EmployeeForm(user=user)
        for field_name, field in employee_form.fields.items():
            self.fields[field_name] = field

        # Добавление полей Customer
        customer_form = CustomerForm()
        for field_name, field in customer_form.fields.items():
            if field_name not in self.fields:
                self.fields[field_name] = field

    customer = forms.ModelMultipleChoiceField(
        queryset=Customer.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={"class": "form-check"}),
        label="Выберите или создайте нового",
        required=False,
    )

    class Meta:
        model = Employee
        fields = "__all__"


MONTHS = {
    1: "Январь",
    2: "Февраль",
    3: "Март",
    4: "Апрель",
    5: "Май",
    6: "Июнь",
    7: "Июль",
    8: "Август",
    9: "Сентябрь",
    10: "Октябрь",
    11: "Ноябрь",
    12: "Декабрь",
}


class MonthYearForm(forms.Form):
    month = forms.ChoiceField(choices=[(i, MONTHS[i]) for i in range(1, 13)])
    year = forms.ChoiceField(choices=[(i, i) for i in range(2024, 2031)])


class WorkDayForm(forms.ModelForm):
    class Meta:
        model = WorkDay
        fields = ["date", "salary"]


def get_person_info(vacation):
    """
    Получает информацию о человеке (сотрудник или пользователь)
    """
    if vacation.employee:
        return f"{vacation.employee.last_name} {vacation.employee.first_name[0]}."
    elif vacation.user:
        return f"{vacation.user.last_name} {vacation.user.first_name[0]}."
    return "неизвестный сотрудник"


class VacationForm(forms.ModelForm):
    start_date = forms.DateField(
        widget=forms.DateInput(
            attrs={"type": "date", "class": "form-control"}, format="%Y-%m-%d"
        ),
        label="Дата начала отпуска",
        required=False,
    )
    end_date = forms.DateField(
        widget=forms.DateInput(
            attrs={"type": "date", "class": "form-control"}, format="%Y-%m-%d"
        ),
        label="Дата окончания отпуска",
        required=False,
    )
    user = forms.ModelChoiceField(
        queryset=User.objects.all(),
        required=False,  # Делаем поле необязательным
        widget=forms.Select(attrs={"class": "form-control"}),
        label="Пользователь",
    )

    def clean(self):
        cleaned_data = super().clean()

        if not cleaned_data.get("employee"):
            cleaned_data["employee"] = None
            cleaned_data["user"] = self.initial.get("user")

        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")

        # Проверка корректности дат только для user, без проверки для employee
        if cleaned_data.get("user") and start_date and end_date:
            if start_date > end_date:
                error_message = f'Дата начала отпуска ({start_date.strftime("%d.%m.%Y")}) не может быть позже даты окончания ({end_date.strftime("%d.%m.%Y")}).'
                raise ValidationError({"start_date": error_message})

            # Проверка пересечения дат с существующими отпусками только для user
            existing_vacations = Vacation.objects.filter(
                Q(user=cleaned_data.get("user"))
                & ~Q(employee__isnull=False),  # Исключаем отпуска с employee
                status__in=["pending", "approved"],
                start_date__lte=end_date,
                end_date__gte=start_date,
            )

            # Если редактируем существующий отпуск, исключаем его из проверки
            if self.instance.pk:
                existing_vacations = existing_vacations.exclude(pk=self.instance.pk)

            if existing_vacations.exists():
                conflicting_vacations = existing_vacations.first()
                person_info = get_person_info(conflicting_vacations)

                error_fields = {}

                # Проверка start_date
                if (
                        start_date >= conflicting_vacations.start_date
                        and start_date <= conflicting_vacations.end_date
                ):
                    error_fields["start_date"] = (
                        f'Отпуск пересекается с отпуском {person_info} с {conflicting_vacations.start_date.strftime("%d.%m.%Y")} по {conflicting_vacations.end_date.strftime("%d.%m.%Y")}'
                    )

                # Проверка end_date
                if (
                        end_date >= conflicting_vacations.start_date
                        and end_date <= conflicting_vacations.end_date
                ):
                    error_fields["end_date"] = (
                        f'Отпуск пересекается с отпуском {person_info} с {conflicting_vacations.start_date.strftime("%d.%m.%Y")} по {conflicting_vacations.end_date.strftime("%d.%m.%Y")}'
                    )

                if error_fields:
                    raise ValidationError(error_fields)

        return cleaned_data

    class Meta:
        model = Vacation
        fields = "__all__"
