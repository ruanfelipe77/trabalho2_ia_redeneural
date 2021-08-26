from django import forms

class AutomacaoForms(forms.Form):
  peso = forms.DecimalField(label="Peso")
  cilindros = forms.DecimalField(label="Cilindros")
  aceleracao = forms.DecimalField(label="Aceleração")
  anomodelo = forms.IntegerField(label="Ano do Modelo")