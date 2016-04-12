from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.forms.widgets import Select
from django import forms

# Create your models here.

class Campaign(models.Model):
	campaign_title = models.CharField(max_length=200)
	start_date = models.DateTimeField('date published')
	campaign_description = models.TextField()
	num_tips = models.IntegerField()
	amount_crowdfunded = models.DecimalField(max_digits=5, decimal_places=2)
	campaign_image = models.ImageField()	
	#"Hacky" fix for images not loading - add a field for url
	campaign_image_url = models.URLField()
	#class Contribution(models.Model):
	stat_1=models.CharField(max_length=25)
	stat_1_description=models.TextField()
	stat_2=models.CharField(max_length=25)
	stat_2_description=models.TextField()
	stat_3=models.CharField(max_length=25)
	stat_3_description=models.TextField()

	def __unicode__(self):
		return "{}".format(self.campaign_title)

class CrowdcopUser(models.Model):
	user=models.OneToOneField(User, on_delete=models.CASCADE)
	institution=models.CharField(max_length=100)
	def get_contributions(self):
		return Contribution.select().where(Contribution.user==self.user)

class Contribution(models.Model):
	user=models.ForeignKey(
		User,
		related_name='contributions'
		)
	amount = models.DecimalField(max_digits=5, decimal_places=2)
	campaign = models.ForeignKey(
		Campaign,
		related_name='contributions'
		)

class Tip(models.Model):
	date=models.DateTimeField()
	#Location will be a zip code for now
	location=models.TextField()

	#Suspect information 
	suspect_identity=models.TextField()
	suspect_gender=models.CharField(max_length=20)
	suspect_race=models.CharField(max_length=100)
	suspect_eye_color=models.CharField(max_length=20)
	suspect_hair_color=models.CharField(max_length=20)
	suspect_hair_style=models.CharField(max_length=30)
	suspect_features=models.TextField()
	suspect_other=models.TextField()


class PayPalID(models.Model):
	contact_name=models.CharField(max_length=100)
	paypal_username=models.CharField(max_length=100)
	contact_info=models.TextField()