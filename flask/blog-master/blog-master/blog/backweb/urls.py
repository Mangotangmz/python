from django.contrib.auth.decorators import login_required
from django.urls import path

from backweb import views


urlpatterns = [
    # 登录
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('index/', login_required(views.Index.as_view()), name='index'),
    path('add_article/', login_required(views.AddArticle.as_view()), name='add_article'),
    path('get_ctypes/', login_required(views.GetCtypes.as_view()), name='get_ctypes'),
    path('del_article/<int:id>/', login_required(views.DelArticle.as_view()), name='del_article'),
    path('edit_article/<int:id>/', login_required(views.EditArticle.as_view()), name='edit_article'),
    path('change_pwd/', login_required(views.ChangePwd.as_view()), name='change_pwd'),
    path('change_art_show/<int:id>/', login_required(views.ChangeArtShow.as_view()), name='change_art_show'),
    path('change_art_recommend/<int:id>/', login_required(views.ChangeArtRecommend.as_view()), name='change_art_recommend'),
]
