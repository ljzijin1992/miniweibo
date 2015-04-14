#! -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from account.views import login
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'miniweibo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^$',login),
	url(r'^account/', include('account.urls')),
)
