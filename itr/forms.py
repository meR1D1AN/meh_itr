from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    date_registration = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Дата регистрации')
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Дата рождения')
    hire_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Дата приема на работу')
    issued_when = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Дата выдачи паспорта', required=False)
    date_of_termination = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Дата увольнения', required=False)

    class Meta:
        model = Employee
        fields = '__all__'  # Добавляем все поля, если это необходимо

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Получаем текущего пользователя
        super(EmployeeForm, self).__init__(*args, **kwargs)

        if not user.is_superuser:
            # Если пользователь не администратор, скрываем поле "created_by"
            self.fields['created_by'].widget = forms.HiddenInput()
