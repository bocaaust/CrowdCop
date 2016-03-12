"""crowdcop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from . import views

handler404 = 'crowdcop_web.views.error_404'


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^campaign/(?P<campaign_id>[0-9]+)/$', views.campaign, name='campaign'),
    url(r'^profile', views.profile, name='profile'),
    url(r'^404', views.error_404, name='404'),
    url(r'^creators', views.creators, name='creators'),
    url(r'^faq', views.faq, name='faq'),
]
