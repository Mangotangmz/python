# -*- coding:utf-8 -*-
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, render_to_response
from django.views.generic.base import View

from backweb.models import Article, AType
from blog.settings import ARTICLE_NUMBER


class Index(View):
    """
    首页
    """
    def get(self, *args, **kwargs):
        # 过滤is_show为True的文章
        articles = Article.objects.filter(is_show=True)[:13]
        atypes = AType.objects.filter(~Q(f_typeid=None))
        return render_to_response('web/index.html', {'articles': articles, 'atypes': atypes})


class About(View):
    """
    关于我
    """
    def get(self, *args, **kwargs):
        return render_to_response('web/about.html')


class Menu(View):
    """
    菜单信息--> 文章分类和站长推荐
    """
    def get(self, *args, **kwargs):
        articles = Article.objects.filter(is_recommend=True)[:5]
        atypes = AType.objects.filter(~Q(f_typeid=None))
        articles = [article.to_dict() for article in articles]
        atypes = [atype.to_dict() for atype in atypes]
        return JsonResponse({'articles': articles, 'atypes': atypes})


class Info(View):
    """
    文章详情页
    """
    def get(self,*args, **kwargs):
        id = kwargs['id']
        articles = Article.objects.all()
        article = articles.filter(id=id).first()
        articles_ids = [article.id for article in articles]
        current_i = 0
        for i in range(len(articles_ids)):
            if articles_ids[i] == id:
                current_i = i
                break;
        # 获取上一页和下一页的文章
        next, last = '', ''
        if current_i != 0:
            last = articles.filter(id=articles_ids[current_i-1]).first()

        if current_i != len(articles_ids) -1:
            next = articles.filter(id=articles_ids[current_i + 1]).first()

        return render_to_response('web/info.html', {'article': article, 'last': last, 'next': next})


class List(View):
    """
    文章列表页
    """
    def get(self, request, *args, **kwargs):
        atype = request.GET.get('type')
        try:
            page = int(request.GET.get('page', 1))
        except Exception as e:
            page = 1
        if atype:
            articles = Article.objects.filter(types__types=atype)
        else:
            articles = Article.objects.all()
        paginator = Paginator(articles, ARTICLE_NUMBER)
        articles = paginator.page(page)
        return render_to_response('web/list.html', {'articles': articles, 'atype': atype})


class Search(View):
    """
    搜索页面
    """
    def get(self, request, *args, **kwargs):
        search_params = request.GET.get('search_params')
        try:
            page = int(request.GET.get('page', 1))
        except Exception as e:
            page = 1
        articles = Article.objects.filter(Q(title__icontains=search_params) | Q(types__types__icontains=search_params))
        paginator = Paginator(articles, ARTICLE_NUMBER)
        articles = paginator.page(page)
        return render_to_response('web/search.html', {'articles': articles, 'search_params': search_params})

