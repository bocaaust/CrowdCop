from django import forms
from .models import CrowdcopUser, Contribution, Tip, PayPalID, Campaign
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
	campaign=forms.ModelChoiceField(queryset=Campaign.objects.all())

	class Meta:
		model= Tip
		fields = ('date', 'location','suspect_identity','suspect_gender','suspect_race','suspect_eye_color','suspect_hair_color','suspect_features','suspect_other',)

class PaypalForm(forms.ModelForm):
	class Meta:
		model = PayPalID
		fields = ('contact_name', 'paypal_username', 'contact_info',)