from django.contrib import admin

from models import Campaign, CrowdcopUser, Tip, PayPalID

# Register your models here.
admin.site.register(Campaign)
admin.site.register(CrowdcopUser)
admin.site.register(Tip)
admin.site.register(PayPalID)
