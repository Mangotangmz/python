
from django.http import HttpResponseRedirect
from django.urls import reverse


def is_login(func):

    def check(request):
        try:
            # 获取session中已经保存的user_id的值
            request.session['user_id']

        except:
            # 跳转登录
            return  HttpResponseRedirect(reverse('users:login'))
        return  func(request)
    return check