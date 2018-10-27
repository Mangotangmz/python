import logging
import time

from django.utils.deprecation import  MiddlewareMixin

from users.models import MyUser


class UserAuthMeiddleware(MiddlewareMixin):
    def process_request(self,request):

        user = MyUser.objects.get(username='admin')
        request.user = user
        return None

class LogMiddleware(MiddlewareMixin):
    def process_request(self,request):
#         url到服务器的时候，经过中间件最先执行的方法
        request.init_time = time.time()
        request.init_body = request.body

    def process_response(self,request,response):
        # 经过中间件，最后执行的方法
        count_time = (time.time()-request.init_time)*1000
        # 响应状态
        code = response.statu_code
        req_body = response.init_body
        res_body = response.content

        # 获取logger
        logger = logging.getLogger(__name__)
        msg ='%s %s %s %s'%(count_time,code,req_body,res_body)
        logger.info(msg)
        return response