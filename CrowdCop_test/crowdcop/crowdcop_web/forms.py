from django import forms
from .models import CrowdcopUser, Contribution, Tip, PayPalID, Campaign
from django.contrib.auth.models import User
from captcha.fields import CaptchaField
from django.forms import Textarea, SelectDateWidget
class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'email', 'first_name', 'last_name','password')

class CrowdcopUserForm(forms.ModelForm):
	class Meta:
		model = CrowdcopUser
		fields = ('institution',)

class CrimeDetailForm(forms.ModelForm):
	class Meta:
		model= Tip
		fields = ('details','date', 'location','campaign',)

class SuspectForm(forms.ModelForm):
	class Meta:
		model=Tip
		fields = ('suspect_identity','suspect_gender','suspect_race','suspect_eye_color','suspect_hair_color','suspect_hair_style','suspect_features','suspect_other',)

class PaypalForm(forms.ModelForm):
	class Meta:
		model = PayPalID
		fields = ('contact_name', 'paypal_username', 'contact_info',)

class CaptchaForm(forms.Form):
  	captcha = CaptchaField()

class CrowdfundForm(forms.Form):
	amount = forms.DecimalField(max_digits=5, decimal_places=2)
