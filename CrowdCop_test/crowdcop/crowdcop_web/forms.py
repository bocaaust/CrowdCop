from django import forms
from .models import CrowdcopUser, Contribution
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'email', 'first_name', 'last_name','password')

class CrowdcopUserForm(forms.ModelForm):
	class Meta:
		model = CrowdcopUser
		fields = ('institution',)