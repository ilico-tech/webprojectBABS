import django_filters
from .models import Voiture
from django import forms



class VoitureFilter(django_filters.FilterSet):


         class Meta:
                model = Voiture
                fields = ['emplacement','service']

         widgets ={
             'emplacement':forms.TextInput(attrs={'class': 'form-control','style':'width:150px; height:30px'}),
             'service':forms.Select(attrs={'class': 'form-control'}),
         }


