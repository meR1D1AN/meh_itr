from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'  # Добавляем все поля, если это необходимо

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Получаем текущего пользователя
        super(EmployeeForm, self).__init__(*args, **kwargs)

        if not user.is_superuser:
            # Если пользователь не администратор, скрываем поле "created_by"
            self.fields['created_by'].widget = forms.HiddenInput()
