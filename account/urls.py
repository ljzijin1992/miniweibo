#! -*- coding:UTF-8 -*-
from django.conf.urls import patterns, include, url
from account import views

urlpatterns = patterns('',
	url(r'^$', views.login),
	url(r'^login/',views.accountlogin),
	url(r'^register/',views.register),
	url(r'^userregister/',views.accountregister),
)