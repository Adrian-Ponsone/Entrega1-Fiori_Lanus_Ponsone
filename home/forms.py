from unicodedata import name
from django import forms

class UserForm(forms.Form):
    name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    creation_date = forms.DateField(required=False)
    
    
class SearchUserForm(forms.Form):
    name = forms.CharField(max_length=30, required=False)