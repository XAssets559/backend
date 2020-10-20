# from django.shortcuts import render
from user.models import Task,User
from blog.models import Article
from user.serializers import TaskListSerializer
from blog.serializers import ArticleListSerializer
from django.http import HttpResponse,JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.sessions.models import Session



# Create your views here.
class Task_listView(APIView):
    def get(self,request):
        change = False#用来判断是否是编辑页面
        try:#教师后台页面的任务管理列表
            change = request.GET['change']
            sess = Session.objects.get(pk=request.COOKIES['sessionid'])
            user = User.objects.get(nick_name=sess.get_decoded().get('nick_name'))
            task_set = user.task.all()
            serializer = TaskListSerializer(task_set, many=True)
            return  JsonResponse(serializer,safe=False,status=status.HTTP_200_OK)
        except:#主页的任务列表
            task_set = Task.objects.all()#返回所有的任务
            serializer = TaskListSerializer(task_set,many=True)
            return JsonResponse(serializer.data,safe=False,status=status.HTTP_200_OK)



class Article_listView(APIView):
    def get(self,request):
        change = False
        try:#自己的文章编辑页面的列表
            change = request.GET['change']
            sess = Session.objects.get(pk=request.COOKIES['sessionid'])
            user = User.objects.get(nick_name=sess.get_decoded().get('nick_name'))
            article_set = user.article.all()
            serializer = ArticleListSerializer(article_set,many=True)
            return JsonResponse(serializer.data, safe=False,status=status.HTTP_200_OK)
        except:#主页的文章列表
            if Article.objects.count() <= 3:
                article_set = Article.objects.all()
            else:
                article_set = Article.objects.all()[:3]#返回前三篇文章
            serializer = ArticleListSerializer(article_set,many=True)
            return JsonResponse(serializer.data,safe=False,status=status.HTTP_200_OK)

class Test(APIView):
    def get(self,request):
        data = HttpResponse('success').set_cookie('nick_name','xiahaitao')
        ty = type(data)
        print(data)
        return HttpResponse('success')
