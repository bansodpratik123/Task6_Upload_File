from .models import Cities
from django import forms

class CitiesModelForm(forms.ModelForm):
    class Meta:
        model=Cities
        fields='__all__'