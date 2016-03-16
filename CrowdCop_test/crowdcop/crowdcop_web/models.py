from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

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
	