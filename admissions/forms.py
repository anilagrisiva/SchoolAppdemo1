from django import forms
from admissions.models import Students


class admiModelForm(forms.ModelForm):
    class Meta:
        model=Students
        fields='__all__'
