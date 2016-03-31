from django import forms
from .models import CrowdcopUser, Contribution, Tip, PayPalID
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

class TipForm(forms.ModelForm):
	class Meta:
		model= Tip
		fields = ('tip', 'date', 'location')

class PaypalForm(forms.ModelForm):
	class Meta:
		model = PayPalID
		fields = ('paypal_username',)