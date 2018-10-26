
from django.conf.urls import url

from home import views


urlpatterns = [
    # 主页
    url(r'index/', views.index, name='index'),
]