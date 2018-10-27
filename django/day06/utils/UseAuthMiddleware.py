from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseRedirect, HttpResponse

from users.models import UserTicket


class UserMiddleware(MiddlewareMixin):
    # 重构拦截方法
    def process_request(self,request):

        # 排除不需要的登录验证的地址
        not_login_path =['/users/login/','/users/register/']
        path = request.path
        # 校验不需要登录验证的地址
        for n_path in not_login_path:
            # 如果当前访问的地址为登录地址或者注册地址，则直接访问对应的视图函数
            if path == n_path:
                return None

        ticket = request.COOKIES.get('ticket')

        # 如果请求中的cookie中没有ticket，则跳转登录
        if not ticket:
            return HttpResponseRedirect(reverse('users:login'))
        # 通过tickt参数获取当前登录用户的信息
        user_ticket = UserTicket.objects.filter(ticket=ticket).first()
        if not user_ticket:
            return HttpResponseRedirect(reverse('users:login'))
        #  设置全局user
        request.user = user_ticket.user
        # 中间件执行结束，可返回None或者不写
        return None

