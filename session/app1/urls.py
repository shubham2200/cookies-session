from django.contrib import admin
from django.urls import path , include
from .views import *

urlpatterns = [
    path('',set_session, name='set_session'),
    path('get/' , get_session , name='get'),
    path('del/' , del_session , name='del')
]
