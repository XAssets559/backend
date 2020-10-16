from django.shortcuts import render
from user.models import Task
from blog.models import Article
from user.serializers import TaskSerializer
from blog.serializers import ArticleSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.
class Task_listView(APIView):
    def get(self,request):
        change = False#用来判断是否是编辑页面
        try:
            change = request.GET['change']
            return  JsonResponse('success',safe=False)
        except:
            task_set = Task.objects.all()#返回所有的任务
            serializer = TaskSerializer(task_set,many=True)
            return JsonResponse(serializer.data,safe=False)



class Article_listView(APIView):
    def get(self,request):
        article_set = Article.objects.all()#返回所有的任务
        serializer = ArticleSerializer(article_set,many=True)
        return JsonResponse(serializer.data,safe=False)