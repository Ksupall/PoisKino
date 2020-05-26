from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class SearchForm(forms.Form):
	name = forms.CharField(
		max_length=100,
		widget=forms.TextInput(
			attrs={ 'class': 'form-control'}
		)
	)
