


from django.conf.urls import url, include
from django.contrib import admin


from users import views


urlpatterns = [
    url(r'^login/', views.login, name='login'),
    url(r'^index/', views.index, name='index'),
    url(r'^logout/',views.logout,name='logout')
]