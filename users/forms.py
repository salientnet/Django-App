from django import forms
from users.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'birthday', 'random_number']
        widgets = {
        	'username': forms.TextInput(attrs = {"class": "form-control"}),
        	'birthday': forms.DateInput(attrs = {"class": "form-control"}),
        	'random_number': forms.NumberInput(attrs = {"class": "form-control"})
        }
