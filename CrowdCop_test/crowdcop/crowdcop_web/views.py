from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Campaign, CrowdcopUser
from .forms import UserForm, CrowdcopUserForm, CrimeDetailForm, SuspectForm, PaypalForm, CaptchaForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.core.mail import send_mail, BadHeaderError
import math
from django.contrib.auth.models import User

# Create your views here.
def index(request):
	latest_campaigns= Campaign.objects.order_by('-start_date')[:9]
	trending_campaigns=Campaign.objects.order_by('amount_crowdfunded')[:6]
	num_pages=int(math.ceil((Campaign.objects.count())/6))+1
	inactive_page=num_pages+1
	pages = []
	for i in range(1,(num_pages+1)):
		pages.append(i)
	return render(request, 'crowdcop_web/index_template.html',{'latest_campaigns': latest_campaigns, 
		'trending_campaigns': trending_campaigns, 'current_page':1,'previous_page':0,'next_page':2,
	 'num_pages':num_pages,'pages':pages,'inactive_page': inactive_page,})

def campaign(request, campaign_id):
	campaign = get_object_or_404(Campaign, pk=campaign_id)
	following = False
	try:
		user_profile=request.user.profile
	except CrowdcopUser.DoesNotExist:
		user_profile = CrowdcopUser.objects.create(user=request.user)
	if request.user.is_authenticated and user_profile.following.filter(id=campaign_id).exists():
		following=True
	return render(request, 'crowdcop_web/campaign_template.html', 
		{'campaign':campaign, 'following':following})

def profile(request):
	user_profile=request.user.profile
	campaigns=user_profile.following.all()
	return render(request, 'crowdcop_web/profile_template.html', {'user_profile': user_profile, 'campaigns':campaigns})

def error_404(request):
	return render(request, 'crowdcop_web/404_template.html')

def creators(request):
	return render(request, 'crowdcop_web/creator_template.html')

def faq(request):
	return render(request, 'crowdcop_web/faq_template.html')


def trending(request, page):
	start=6*(int(page)-1)
	end=6*int(page)
	num_pages=int(math.ceil((Campaign.objects.count())/6))+1
	previous_page=(int(page))-1
	next_page=(int(page))+1
	pages = []
	for i in range(1,(num_pages+1)):
		pages.append(i)
	inactive_page=num_pages+1
	latest_campaigns= Campaign.objects.order_by('-start_date')[:9]
	trending_campaigns=Campaign.objects.order_by('amount_crowdfunded')[start:end]
	return render(request, 'crowdcop_web/index_template.html',{'latest_campaigns': latest_campaigns,
	 'trending_campaigns': trending_campaigns, 'current_page':page,'previous_page':previous_page,'next_page':next_page,
	 'num_pages':num_pages,'pages':pages,'inactive_page': inactive_page,})

def trending_blank(request):
	start=0
	end=6
	num_pages=int(math.ceil((Campaign.objects.count())/6))+1
	previous_page=0
	next_page=2
	pages = []
	for i in range(1,(num_pages+1)):
		pages.append(i)
	inactive_page=num_pages+1
	latest_campaigns= Campaign.objects.order_by('-start_date')[:9]
	trending_campaigns=Campaign.objects.order_by('amount_crowdfunded')[start:end]
	return render(request, 'crowdcop_web/index_template.html',{'latest_campaigns': latest_campaigns,
	 'trending_campaigns': trending_campaigns, 'current_page':1,'previous_page':previous_page,'next_page':next_page,
	 'num_pages':num_pages,'pages':pages,'inactive_page': inactive_page,})

def register(request):
	registered= False

	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = CrowdcopUserForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()

        	#Hash password
			user.set_password(user.password)
			user.save()
			profile = profile_form.save(commit=False)
			profile.user = user

			profile.save()

			registered=True            
		else:
			print user_form.errors, profile_form.errors

	else:
		user_form = UserForm()
		profile_form = CrowdcopUserForm()

	return render(request,
			'crowdcop_web/register.html',
			{'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

def user_login(request):
	if request.method == 'POST':
		username=request.POST['username']
		password=request.POST['password']

		user=authenticate(username=username,password=password)

		if user:
			if user.is_active:
				login(request,user)
				return HttpResponseRedirect('/crowdcop_web/')
			else:
				return HttpResponse("Your CrowdCop account has been disabled.")
		else:
			#Bad login
			return HttpResponse("Invalid username or password.")
	else:
		return render(request,'crowdcop_web/login_template.html', {})

@login_required
def user_logout(request):
	# Since we know the user is logged in, we can now just log them out.
	logout(request)

	# Take the user back to the homepage.
	return HttpResponseRedirect('/crowdcop_web/')

def submit_tip(request):

	if request.method== 'POST':
		tip_form=CrimeDetailForm(data=request.POST)
		suspect_form=SuspectForm(data=request.POST)
		paypal_form=PaypalForm(data=request.POST)
		captcha_form=CaptchaForm(request.POST)
		email_message=""
		if tip_form.is_valid() and captcha_form.is_valid():
			tip = tip_form.save()
			suspect = suspect_form.save()
			paypal_id=paypal_form.save()
			tip_data = serializers.serialize("xml", [tip])
			suspect_data=serializers.serialize("xml",[suspect])

			email_message= tip_data + suspect_data
			print email_message
			paypal_data=serializers.serialize("xml",[paypal_id])

	        try:
	        	send_mail("Crime Tip", email_message, 'tips@crowdcop.io', ['tips@crowdcop.io'])
	        except BadHeaderError:
	        	return HttpResponse('Invalid header found.')
			
			return HttpResponseRedirect('/crowdcop_web/')
		else:
			print tip_form.errors, captcha_form.errors
	else:
		tip_form=CrimeDetailForm()
		suspect_form=SuspectForm()
		paypal_form=PaypalForm()
		captcha_form=CaptchaForm()
	return render(request, 'crowdcop_web/tip_template.html',
		{'tip_form': tip_form, 'suspect_form': suspect_form, 'paypal_form':paypal_form, 'captcha_form': captcha_form})	

def follow(request, campaign_id):
	campaign_to_follow=get_object_or_404(Campaign,pk=campaign_id)
	try:
		user_profile=request.user.profile
	except CrowdcopUser.DoesNotExist:
		user_profile = CrowdcopUser.objects.create(user=request.user)	
	if user_profile.following.filter(id=campaign_to_follow.id).exists():
		return HttpResponse('You already follow this campaign.')
	else:
		user_profile.following.add(campaign_to_follow)
		return HttpResponseRedirect('/crowdcop_web/campaign/'+campaign_id)

def unfollow(request, campaign_id):
	campaign_to_unfollow=get_object_or_404(Campaign,pk=campaign_id)
	try:
		user_profile=request.user.profile
	except CrowdcopUser.DoesNotExist:
		user_profile = CrowdcopUser.objects.create(user=request.user)	
	if user_profile.following.filter(id=campaign_to_unfollow.id).exists():
		user_profile.following.remove(campaign_to_unfollow)
		return HttpResponseRedirect('/crowdcop_web/campaign/'+campaign_id)
	else:
		return HttpResponse('You aren\'t following this campaign.')
		
