
from django.urls import path

from app import views


urlpatterns = [
    path('index/', views.Index.as_view(), name='index'),
    path('about/', views.About.as_view(), name='about'),
    path('menu/', views.Menu.as_view(), name='menu'),
    path('info/<int:id>/', views.Info.as_view(), name='info'),
    path('list/', views.List.as_view(), name='list'),
    path('search/', views.Search.as_view(), name='search'),
]
