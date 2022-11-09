from socket import fromshare
from django.db import models
from func.models import Contato
from django import forms 

class FormContato(forms.ModelForm):
    class Meta:
        model = Contato
        exclude = ()