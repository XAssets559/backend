# -*- coding: utf-8 -*-
# @Time    : 2020/10/10 22:39
# @Author  : Mr.Xia
# @FileName: urls.py
# @Software: PyCharm

from django.urls import path,include
from .views import *

urlpatterns = [
    path('login/',Login.as_view()),
    path('register/',Register.as_view()),
]