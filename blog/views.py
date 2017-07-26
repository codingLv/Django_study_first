# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Article,Category,Tag
from django.shortcuts import get_object_or_404
# Create your views here.

def index(request):
    '''
    博客首页
    '''
    #all() 方法从数据库里获取了全部的文章，存在了 post_list 变量,博客文章列表是按文章发表时间倒序排列的
    article_list = Article.objects.all().order_by('-created_time')

    #文章列表数据的 post_list 变量传给了模板
    return render(request, 'index.html', context={'article_list':article_list})

def detail(request,id):
    '''
    文章详情
    传入请求和文章的id
    get_object_or_404()方法
    其作用:
    当传入的 id 对应的 Post 在数据库存在时，就返回对应的 article。
    如果不存在，就给用户返回一个 404 错误，表明用户请求的文章不存在。
    '''
    article = get_object_or_404(Article,id=id)
    return render(request, 'detail.html', context={'article':article})

def archives(request, year, month):
    #注意created_time__year后面是两个下划线
    article_list = Article.objects.filter(created_time__year=year,created_time__month=month).order_by('-created_time')
    return render(request, 'index.html', context={'article_list':article_list})

def category(request,id):
    cate = get_object_or_404(Category,id=id)
    article_list = Article.objects.filter(category=cate).order_by('-created_time')

    return render(request, 'index.html', context={'article_list':article_list})
