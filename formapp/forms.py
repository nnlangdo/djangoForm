from unicodedata import name
from django import forms
from importlib_metadata import email
from matplotlib.pyplot import cla

class PersonalForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
