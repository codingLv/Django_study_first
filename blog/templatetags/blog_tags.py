# -*- coding:utf-8 -*-

from django import template
from ..models import Article,Category
from django .db.models.aggregates import Count

register = template.Library()
#最新文章  num=4代表显示最近的三篇文章

@register.simple_tag
def get_recent_article(num=3):
    return Article.objects.all().order_by('-created_time')[:num]

@register.simple_tag
def archives():
    #month是精度，精确到月
    return Article.objects.dates('created_time','month',order='DESC')

@register.simple_tag
def get_categories():
    Category_list=Category.objects.annotate(num_article = Count('article'))
    return Category_list
