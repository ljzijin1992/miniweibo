#! -*- coding: utf-8 -*-
from django.db import models

#一条微博
class Timeline(models.Model):
	#avatar = models.ImageField()
	content = models.TextField()#weibo内容
	created_at = models.DateTimeField(auto_now_add=True)#创建时间
	
	class Meta(object):
		db_table = 'timeline'

#微博的评论
class Comment(models.Model):
	timeline = models.ForeignKey(Timeline,related_name="timeline_comments")
	content = models.TextField()#评论内容
	created_at = models.DateTimeField(auto_now_add=True)#创建时间

	class Meta(object):
		db_table = "timeline_comment"
