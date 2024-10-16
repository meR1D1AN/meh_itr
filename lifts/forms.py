from django import forms
from .models import Problem


class ProblemForm(forms.ModelForm):
    class Meta:
        model = Problem
        fields = [
            "problem"
        ]  # Указываем только описание проблемы, "resolved" автоматически False
        labels = {"problem": "Описание проблемы"}
