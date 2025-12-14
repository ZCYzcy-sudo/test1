from booktest import views
from django.urls import re_path

urlpatterns = [
    re_path(r'^$', views.index),
    re_path(r'^zhouchengyi', views.zhouchengyi),
    re_path(r'^login', views.login, name='login'),
    re_path(r'^register', views.register, name='register'),
    re_path(r'^reader_home', views.reader_home, name='reader_home'),
]