from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
	return render(request, 'crowdcop_web/index_template.html')

def campaign(request):
	return render(request, 'crowdcop_web/campaign_template.html')

def profile(request):
	return render(request, 'crowdcop_web/profile_template.html')

			