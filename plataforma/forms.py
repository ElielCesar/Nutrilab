from django import forms
from .models import Pacientes

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Pacientes
        fields = ['nome', 'sexo', 'idade', 'email', 'telefone']

        widgets = {

            'nome':forms.TextInput(attrs={'class':'form-control'}),
            'sexo':forms.Select(attrs={'class':'form-control'}),
            'idade':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'telefone':forms.TextInput(attrs={'class':'form-control'}),
        }


