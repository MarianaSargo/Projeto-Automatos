from django.forms import ModelForm
from .models import Automato, MTuring

from django import forms

class AutomatoForm(ModelForm):
    class Meta:
        model = Automato
        fields = '__all__'

        widgets = {
            'EstadoInicial': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'descrição do automato...'}),
            'EstadoFinal': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'descrição do automato...'}),
            'Alfabeto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'descrição do automato...'}),
            'Transicoes': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'descrição do automato...'}),
            'Descricao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'descrição do automato...'}),
            'Estados': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'descrição do automato...'}),

        }

class MTuringForm(ModelForm):
    class Meta:
        model = MTuring
        fields = '__all__'

        widgets = {
            'EstadoInicial': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'descrição da MT...'}),
            'EstadoFinal': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'descrição da MT...'}),
            'Alfabeto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'descrição da MT...'}),
            'Transicoes': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'descrição da MT...'}),
            'Descricao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'descrição da MT...'}),
            'Estados': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'descrição da MT...'}),
        }



class ExpressaoForm(forms.Form):
    expressao = forms.CharField()

class ExpressaoMTForm(forms.Form):
    expressaoMT = forms.CharField()
