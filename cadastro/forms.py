from django import forms

from cadastro.models import Cidade, State


class CidadeForm(forms.ModelForm):
    class Meta:
        model = Cidade
        fields = '__all__'  # Imports all fields. Conversely, I can select


class StateForm(forms.ModelForm):
    class Meta:
        model = State
        fields = '__all__'
