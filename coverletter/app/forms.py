from django import forms
from .models import *

class PersonForm(forms.ModelForm):
    class Meta:
        model = PersonInfo
        fields = ('PersonName', 'CompanyName')

    