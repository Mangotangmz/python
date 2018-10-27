
import random

from django.http import request
from django.http import HttpResponseRedirect, HttpResponse
from users.models import UserTicket


def get_ticekt():
    s='1234567890qwertyuiopasdfghjklzxcvbnm'
    ticket = ''
    for i in range(25):
        ticket += random.choice(s)
    return ticket

def is_login(func):

    def check(request):
        ticket = request.COOKIES.get('ticket')
        if ticket:
            user_ticket = UserTicket.objects.filter(ticket=ticket).first()
            user = user_ticket.user

            if user_ticket:
                # user = user_ticket.user
                # 返回被装饰的函数index
                return func(request)
            else:
                # 参数错误
                return HttpResponseRedirect(reversed('users:login'))
        else:
        #      没有tickets说明没有登录
            return HttpResponseRedirect(reversed('user:login'))
    return check