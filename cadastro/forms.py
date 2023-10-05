from django import forms

from cadastro.models import Cidade


class CidadeForm(forms.ModelForm):
    class Meta:
        model = Cidade
        fields = '__all__'  # Imports all fields. Conversely, I can select
