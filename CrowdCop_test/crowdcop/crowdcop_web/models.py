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
	user=models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
	institution=models.CharField(max_length=100)
	following = models.ManyToManyField(Campaign)
	def get_contributions(self):
		return Contribution.select().where(Contribution.user==self.user)
	def get_history(self):
		return CampaignView.objects.filter(user=self.user)
	def __unicode__(self):
		return "{}".format(self.user.username)
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
	contribution_date=models.DateTimeField(auto_now_add=True)
	tx=models.CharField(max_length=250)
	def __unicode__(self):
		return "${} towards {} from {} at {}".format(self.amount,self.campaign,self.user,self.contribution_date)
class Tip(models.Model):
	GENDER_CHOICES = (
		('MALE', 'Male'),
		('FEMALE', 'Female'),
		('OTHER', 'Other/Unknown'),
		)
	RACE_CHOICES = (
		('UNKNOWN', 'Unknown'),
		('ASIAN', 'Asian'),
		('BLACK/AFRICAN-AMERICAN', 'Black/African-American'),
		('CAUCASIAN', 'Caucasian'),
		('HISPANIC/LATINO', 'Hispanic/Latino'),
		('NATIVE AMERICAN', 'Native American'),
		('OTHER', 'Other'),
		)
	EYE_COLOR_CHOICES = (
		('UNKNOWN', 'Unknown'),
		('AMBER', 'Amber'),
		('BLACK', 'Black'),
		('BLUE', 'Blue'),
		('BROWN', 'Brown'),
		('GRAY', 'Gray'),
		('GREEN', 'Green'),
		('HAZEL', 'Hazel'),
		('OTHER', 'Other'),
		)
	HAIR_COLOR_CHOICES = (
		('UNKNOWN', 'Unknown'),
		('BLACK', 'Black'),
		('BROWN', 'Brown'),
		('GRAY', 'Gray'),
		('BLOND', 'Blond'),
		('RED', 'Red'),
		('OTHER', 'Other'),		
		)
	HAIR_STYLE_CHOICES = (
		('UNKNOWN', 'Unknown'),
		('SHORT', 'Short'),
		('MEDIUM', 'Medium'),
		('LONG', 'Long'),
		('DREADLOCKS', 'Dreadlocks'),
		('BALDING', 'Balding'),
		('BALD/SHAVED', 'Bald/Shaved'),
		('OTHER', 'Other'),	
		)
	details=models.TextField(
		verbose_name='What happened? (Be specific about the alleged crime and any victims).')
	date=models.DateTimeField(
		verbose_name='When did this occur (If known, enter date and time).',
		blank=True,
		null=True)
	#Location will be a zip code for now
	location=models.TextField(
		verbose_name='Where did this occur? (Please be as specific as possible about the location. Include house number, street, color of house, etc.).')
	
	#As the number of campaigns increases, we will replace this drop-down menu with a search bar
	campaign=models.ForeignKey(
		Campaign,
		related_name='campaigns',
		verbose_name='Below is a list of all existing campaigns currently on the CrowdCop website. If any of these campaigns are relevant to your tip, please select it.',
		blank=True,null=True)

	#Suspect information 
	suspect_identity=models.CharField(max_length=128, 
		verbose_name='Who did you see? (If known, enter a name or a name known by)',
		blank=True,
		null=True)
	suspect_gender=models.CharField(choices=GENDER_CHOICES, max_length=30,
		blank=True,
		null=True)
	suspect_race=models.CharField(choices=RACE_CHOICES, max_length=30,
		blank=True,
		null=True)
	suspect_eye_color=models.CharField(choices=EYE_COLOR_CHOICES,max_length=20,
		blank=True,
		null=True)
	suspect_hair_color=models.CharField(choices=HAIR_COLOR_CHOICES, max_length=20,
		blank=True,
		null=True)
	suspect_hair_style=models.CharField(choices=HAIR_STYLE_CHOICES, max_length=30,
		blank=True,
		null=True)
	suspect_features=models.TextField(
		verbose_name='Scars, Marks, Tattoos, Piercings',
		blank=True, null=True)
	suspect_other=models.TextField(
		verbose_name='Other suspect details (clothing, telephone, employment, etc.)',
		blank=True, null=True)
	approved=models.BooleanField(default=False)

class PayPalID(models.Model):
	contact_name=models.CharField(
		verbose_name='Your Name (not required):', 
		max_length=100,blank=True,null=True)
	paypal_username=models.CharField(
		verbose_name='If you wish to be compensated for your tip, please enter your Paypal username here (Not Required):',
		max_length=100,blank=True,null=True)
	contact_info=models.TextField(
		verbose_name='How can we contact you?',
		blank=True,null=True)

class CampaignView(models.Model):
	user=models.ForeignKey(User, blank=True, null=True, related_name='user')
	campaign = models.ForeignKey(
		Campaign,
		related_name='campaign'
		)
	date=models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		str=""
		try:
			str="\"{}\" viewed by {} on {}".format(self.campaign.campaign_title,self.user.username, self.date)
		except AttributeError:
			str="\"{}\" viewed by an anonymous user on {}".format(self.campaign.campaign_title,self.date)
		return str