from django import forms
from lifts.models import Problem, Replacement


class ProblemForm(forms.ModelForm):
    class Meta:
        model = Problem
        fields = ['problem']


class ReplacementForm(forms.ModelForm):
    class Meta:
        model = Replacement
        fields = ['info_problem']
