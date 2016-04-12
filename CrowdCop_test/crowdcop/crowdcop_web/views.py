from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Campaign
from .forms import UserForm, CrowdcopUserForm, TipForm, PaypalForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
	latest_campaigns= Campaign.objects.order_by('-start_date')[:9]
	trending_campaigns=Campaign.objects.order_by('amount_crowdfunded')[:6]
	return render(request, 'crowdcop_web/index_template.html',{'latest_campaigns': latest_campaigns, 'trending_campaigns': trending_campaigns, 'page':1,})

def campaign(request, campaign_id):
	campaign = get_object_or_404(Campaign, pk=campaign_id)

	return render(request, 'crowdcop_web/campaign_template.html', {'campaign':campaign})

def profile(request):
	return render(request, 'crowdcop_web/profile_template.html')

def error_404(request):
	return render(request, 'crowdcop_web/404_template.html')

def creators(request):
	return render(request, 'crowdcop_web/creator_template.html')

def faq(request):
	return render(request, 'crowdcop_web/faq_template.html')


def trending(request, page):
	start=6*(int(page)-1)
	end=6*int(page)
	latest_campaigns= Campaign.objects.order_by('-start_date')[:9]
	trending_campaigns=Campaign.objects.order_by('amount_crowdfunded')[start:end]
	return render(request, 'crowdcop_web/index_template.html',{'latest_campaigns': latest_campaigns, 'trending_campaigns': trending_campaigns, 'page':page,})

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
	tip_form=TipForm()
	paypal_form=PaypalForm()
	return render(request, 'crowdcop_web/tip_template.html',
		{'tip_form': tip_form, 'paypal_form':paypal_form})	