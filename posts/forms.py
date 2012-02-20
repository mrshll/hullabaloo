__author__ = 'mmoutenot'

from django import forms
#import settings

class NewForm(forms.Form):
    body = forms.CharField(max_length=400)
