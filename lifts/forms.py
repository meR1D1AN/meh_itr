from django import forms
from lifts.models import TO


class TOForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = TO
        fields = ['date']
