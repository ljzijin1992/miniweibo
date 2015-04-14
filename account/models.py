#! -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class UserProfile(models.Model):
	username = models.CharField(max_length=32)#用户名
	password = models.CharField(max_length=32)#密码
	tel = models.CharField(max_length=15)#手机
	email = models.EmailField()#邮箱
	address = models.CharField(max_length=256)#地址
	remark = models.TextField()#备注
	created_at = models.DateTimeField(auto_now_add=True)#用户创建时间
	is_deleted = models.BooleanField(default=False)#是否已停用

	class Meta(object):
		db_table = 'account_user_profile'#覆盖数据库表名
