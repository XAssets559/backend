# -*- coding: utf-8 -*-
# @Time    : 2020/10/17 20:04
# @Author  : Mr.Xia
# @FileName: detial_views.py
# @Software: PyCharm

from rest_framework import status
from rest_framework.decorators import api_view
from django.http import JsonResponse
from user.models import Task
from user.serializers import TaskDetialSerializer
from blog.models import Article
from blog.serializers import ArticleDetialSerializer
from rest_framework.parsers import JSONParser
import subprocess
def bianyi(scripts):
    pass

@api_view(['GET','POST'])
def task_detial(request,pk):
    if request.method == 'GET':
        task = Task.objects.get(id = pk)
        serializer = TaskDetialSerializer(task)
        return JsonResponse(serializer.data,safe=False)
    elif request.method == 'POST':
        scripts = JSONParser().parse(request)
        bianyi(scripts['scripts'])
        return JsonResponse('',safe=False)


@api_view(['GET','POST'])
def article_detial(request,pk):
    if request.method =='GET':
        article = Article.objects.get(id = pk)
        serializer = ArticleDetialSerializer(article)
        return JsonResponse(serializer.data,safe=False)
