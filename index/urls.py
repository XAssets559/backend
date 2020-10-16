# -*- coding: utf-8 -*-
# @Time    : 2020/10/13 19:19
# @Author  : Mr.Xia
# @FileName: urls.py
# @Software: PyCharm

from django.urls import path,include
from .views import *

urlpatterns = [
    path('task/',Task_listView.as_view()),
    path('article/',Article_listView.as_view()),
]