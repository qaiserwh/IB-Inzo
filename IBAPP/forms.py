
from logging import PlaceHolder
from django import forms
from django.forms import fields, widgets
from . models import Opinion


#############################################

class OpinionForm(forms.ModelForm):
    class Meta:
        model=Opinion
        fields=[
            'Name',
            'TheComment',
         
        ]        
        widgets ={
            'Name': forms.TextInput(attrs={'type':'text','class':'form-control'}),
            'TheComment':forms.Textarea(attrs={'type':'text','class':'form-control','style':'height: 150px'}),


        }