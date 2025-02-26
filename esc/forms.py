from django import forms

from .models import EscProblem, EscReplace


class EscProblemForm(forms.ModelForm):
    class Meta:
        model = EscProblem
        fields = ["problem"]


class EscReplaceForm(forms.ModelForm):
    class Meta:
        model = EscReplace
        fields = ["replace"]
