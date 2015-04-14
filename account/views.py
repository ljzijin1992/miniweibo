#! -*- coding: utf-8 -*-
from django.shortcuts import render
from account import models
# Create your views here.

def login(request):
	return render(request,'login.html')

def accountlogin(request):
	try:
		querydic=request.POST
		for item in querydic:
			print 'item:'+item+','+querydic[item]
	except Exception,e:
		print e
	return render(request,'index.html')


def register(request):
	return render(request,'register.html')

def accountregister(request):
	try:
		querydic=request.POST
		newuser=models.UserProfile.objects.create(username=querydic['username'],password=querydic['password'],email=querydic['username'])
		newuser.save()

	except Exception,e:
		print e
	return render(request,'index.html')