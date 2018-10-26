
from django.contrib.auth.models import User
from django.contrib import auth
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic.base import View

from backweb.forms import UserLoginForm, ArticleForm, UserChangePwdForm
from backweb.models import Article, AType
from blog.settings import ARTICLE_NUMBER


class Login(View):
    """
    登录页面，使用django提供的User表进行登录和权限校验
    """
    def get(self, request, *args, **kwargs):
        return render(request, 'backweb/login.html')

    def post(self, request, *args, **kwargs):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(request,
                                     username=form.cleaned_data.get('username'),
                                     password=form.cleaned_data.get('password')
                                     )
            if user:
                auth.login(request, user)
                return redirect('backweb:index')
            else:
                data = {'password': '账号密码错误'}
                return render(request, 'backweb/login.html', {'error': data})
        else:
            return render(request, 'backweb/login.html', {'error': form.errors})


class Logout(View):
    """
    注销账户
    """
    def get(self, request, *args, **kwargs):
        auth.logout(request)
        return redirect('backweb:login')


class Index(View):
    """
    管理后台首页地址
    """
    def get(self, request, *args, **kwargs):
        # 语言分类id

        ctype_id = request.GET.get('select_lang')
        art_is_show = request.GET.get('art_is_show')
        art_is_recommend = request.GET.get('art_is_recommend')
        select_lang_name = ''
        try:
            page = request.GET.get('page', 1)
        except Exception as e:
            page = 1
        atypes = AType.objects.filter(f_typeid=None)
        articles = Article.objects.all().order_by('-id')

        # 过滤文章分类
        if ctype_id:
            # django2.0版本中外键的查询，查询字段=对象，或则查询字段__id=id，或则查询字段=id
            articles = articles.filter(types=ctype_id)
            # 当前选择分类名
            select_lang_name = AType.objects.filter(id=ctype_id).first().types
        # 过滤是否展示
        if art_is_show:
            articles = articles.filter(is_show=art_is_show)
        # 过滤是否推荐
        if art_is_recommend:
            articles = articles.filter(is_recommend=art_is_recommend)

        paginator = Paginator(articles, ARTICLE_NUMBER)
        articles = paginator.page(page)
        return render(request, 'backweb/index.html', {'atypes': atypes,
                                                      'page': page,
                                                      'articles': articles,
                                                      'select_lang_name': select_lang_name,
                                                      'is_show': art_is_show,
                                                      'is_recommend': art_is_recommend})


class AddArticle(View):
    """
    发布文章
    """
    def get(self, request, *args, **kwargs):
        atypes = AType.objects.filter(f_typeid=None)
        return render(request, 'backweb/article_detail.html', {'atypes': atypes})

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        # 校验form表单中的参数，使用is_valid()方法校验，验证成功则返回True，否则为False
        if form.is_valid():
            # 使用form表单保存数据
            form.save()
            # 保存成功后，跳转到首页
            return redirect('backweb:index')
        # 如果表单验证失败，则返回错误信息
        # return redirect('backweb:add_article')
        atypes = AType.objects.filter(f_typeid=None)
        return render(request, 'backweb/article_detail.html', {'error': form.errors, 'atypes': atypes})


class GetCtypes(View):
    """
    获取文章分类下具体的子分类
    """
    def get(self, request, *args, **kwargs):
        f_id = request.GET.get('f_id')
        c_types = AType.objects.filter(f_typeid=f_id)
        c_types = [c.to_dict() for c in c_types]
        return JsonResponse({'c_types': c_types})


class DelArticle(View):
    """
    删除文章
    """
    def post(self, request, *args, **kwargs):
        a_id = kwargs['id']
        Article.objects.filter(id=a_id).delete()
        return JsonResponse(data={'code':200})


class EditArticle(View):
    """
    编辑文章
    """

    def get(self, request, *args, **kwargs):
        aid = kwargs['id']
        article = Article.objects.get(id=aid)
        atypes = AType.objects.filter(f_typeid=None)
        return render(request, 'backweb/article_detail.html', {'article': article, 'atypes': atypes})

    def post(self, request, *args, **kwargs):
        aid = kwargs['id']
        article = Article.objects.get(id=aid)

        form = ArticleForm(request.POST, instance=article)
        # 校验form表单中的参数，使用is_valid()方法校验，验证成功则返回True，否则为False
        if form.is_valid():
            # 使用form表单保存数据
            form.save()
            # 保存成功后，跳转到首页
            return redirect('backweb:index')
        else:
            article = Article.objects.get(id=aid)
            atypes = AType.objects.filter(f_typeid=None)
            return render(request, 'backweb/article_detail.html', {'article': article,
                                                                   'error': form.errors,
                                                                   'atypes': atypes})


class ChangePwd(View):
    """
    修改密码
    """
    def get(self, request, *args, **kwargs):
        return render(request, 'backweb/change_pwd.html')

    def post(self, request, *args, **kwargs):
        form = UserChangePwdForm(request.POST)
        if form.is_valid():
            # 修改用户密码
            user = request.user
            user.set_password(request.POST.get('passwd2'))
            user.save()

        return render(request, 'backweb/change_pwd.html', {'error': form.errors})


class ChangeArtShow(View):
    """
    修改文章的展示状态
    """
    def get(self, request, *args, **kwargs):
        id = kwargs['id']
        article = Article.objects.filter(id=id).first()
        if article:
            if article.is_show:
                article.is_show = False
            else:
                article.is_show = True
            article.save()
        # return redirect('backweb:index')
        return redirect('/backweb/index/?art_is_show=0')


class ChangeArtRecommend(View):
    """
    修改文章的推荐状态
    """
    def get(self, request, *args, **kwargs):
        id = kwargs['id']
        article = Article.objects.filter(id=id).first()
        if article:
            if article.is_recommend:
                article.is_recommend = False
            else:
                article.is_recommend = True
            article.save()
        # return redirect('backweb:index')
        return redirect('/backweb/index/?art_is_show=0')
