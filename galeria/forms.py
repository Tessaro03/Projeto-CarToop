from django import forms
from galeria.models import Veiculo 

class VeiculoForms(forms.ModelForm):
    class Meta:
        model = Veiculo
        exclude = ['publicada']
        widgets = {
            'nome':forms.TextInput(attrs={'class':'form-control'}),
            'marca':forms.Select(attrs={'class':'form-control'}),
            'ano':forms.TextInput(attrs={'class':'form-control'}),
            'km':forms.TextInput(attrs={'class':'form-control'}),
            'valor':forms.TextInput(attrs={'class':'form-control'}),
            'tipo':forms.Select(attrs={'class':'form-control'}),        
            'legenda':forms.Textarea(attrs={'class':'form-control'}),
            }
        
