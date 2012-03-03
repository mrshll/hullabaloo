from hullabaloo.settings import STATIC_ROOT

__author__ = 'mmoutenot'

from django import forms
#import settings #settings module was not found, commented out -Alden

class NewForm(forms.Form):
    body = forms.CharField(max_length=400)
    image = forms.ImageField()
