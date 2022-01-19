
from django.contrib import admin
from django.urls import path ,include
from .views import *


urlpatterns = [
    path('', set_cookie,  name='set_cookie'),
    path('get_cookie/' , get_cookie , name='get_cookie'),
    path('del_cookie/' , del_cookie , name='del_cookie')


]