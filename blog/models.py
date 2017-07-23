# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    '''
    文章数据库
    '''
    #文章标题字段 CharField相当于sql里面的char
    title = models.CharField(max_length=70)

    #文章正文字段
    body = models.TextField()

    #文章的创建时间
    created_time =models.DateTimeField()

    def __str__(self):
        return self.title
