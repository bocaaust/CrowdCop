from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from .models import Campaign
from .forms import UserForm, CrowdcopUserForm

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
	context = RequestContext(request)
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
		profile_form = UserProfileForm()

	return render_to_response(
			'crowdcop_web/register.html',
			{'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
			context)