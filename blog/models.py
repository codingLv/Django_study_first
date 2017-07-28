# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import markdown
from django.utils.html import strip_tags
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=70)
    #返回str类型
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Article(models.Model):
    '''
    文章数据库
    '''
    #文章标题字段 CharField相当于sql里面的char
    title = models.CharField(max_length=70)

    #文章正文字段
    body = models.TextField()
    excerpt = models.CharField(max_length=200, blank=True)

    #文章的创建时间
    created_time =models.DateTimeField()

    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

    #获取文章详情
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'id':self.id})

    def save(self, *args, **kwargs):
        #如果没有填写摘要从文本中提取前54个字符赋给excerpt
        if not self.excerpt:
            md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            ])
            self.excerpt = strip_tags(md.covert(self.body))[:54]
        #调用父类的save方法将数据保存到数据库
        super(Article, self).save(*args, **kwargs)
