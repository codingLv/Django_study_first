# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request):

    #all() 方法从数据库里获取了全部的文章，存在了 post_list 变量,博客文章列表是按文章发表时间倒序排列的
    article_list = Article.objects.all().order_by('-created_time')

    #文章列表数据的 post_list 变量传给了模板
    return render(request, 'index.html', context={'article_list':article_list})
