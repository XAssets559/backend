# -*- coding: utf-8 -*-
# @Time    : 2020/10/20 18:41
# @Author  : Mr.Xia
# @FileName: create_views.py
# @Software: PyCharm

from rest_framework.decorators import APIView
from django.http import JsonResponse
from user.serializers import TaskDetialSerializer
from blog.serializers import ArticleDetialSerializer
from django.contrib.sessions.models import Session
from rest_framework import status

class CreateTask(APIView):
    def get(self,request):
        return JsonResponse('success',safe=False)
    def post(self,request):
        sess = Session.objects.get(pk=request.COOKIES['sessionid'])
        new_task = request.POST
        serializer = TaskDetialSerializer(new_task.update({'to_user':sess.get_decoded().get('nick_name')}))
        if serializer.is_valid():
            serializer.save()
            return JsonResponse('success',safe=False,status=status.HTTP_200_OK)
        else:
            return JsonResponse('fail',safe=False,status=status.HTTP_206_PARTIAL_CONTENT)


class CreateArticle(APIView):
    def get(self,request):
        return JsonResponse('success',safe=False)
    def post(self,request):
        sess = Session.objects.get(pk=request.COOKIES['sessionid'])
        new_article = request.POST
        serializer = ArticleDetialSerializer(new_article.update({'to_user':sess.get_decoded().get('nick_name')}))
        if serializer.is_valid():
            serializer.save()
            return JsonResponse('success',safe=False,status=status.HTTP_200_OK)
        else:
            return JsonResponse('fail',safe=False,status=status.HTTP_206_PARTIAL_CONTENT)