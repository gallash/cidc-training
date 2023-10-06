from django import forms
from django.core.exceptions import ValidationError

from cadastro.models import Cidade, State


class CidadeForm(forms.ModelForm):
    class Meta:
        model = Cidade
        fields = '__all__'  # Imports all fields. Conversely, I can select

    # def clean(self):
    #     # Additional cleaning logic, after checking for duplicates in the database?
    #     city_name = self.cleaned_data['nome']
    #     if city_name == 'Itajuba':
    #         raise ValidationError("We cannot save the city {}".format(city_name))


class StateForm(forms.ModelForm):
    class Meta:
        model = State
        fields = '__all__'
