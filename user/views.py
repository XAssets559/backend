from django.shortcuts import render
from .serializers import *
from .models import *
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.

def success():
    '''
    :return:status=200;statusText=OK;data=success
    '''
    return JsonResponse('success',safe=False,status=status.HTTP_200_OK)

def error(message):
    if message == 'error':
        return JsonResponse(message,safe=False,status=status.HTTP_400_BAD_REQUEST)
    else:
        return JsonResponse(message,safe=False,status=status.HTTP_206_PARTIAL_CONTENT)


class Login(APIView):
    '''
    :method:POST,GET
    '''
    def get(self,request):
        return success()

    def post(self,request):
        '''

        :param request:
        :return: message,status
        '''
        data = JSONParser().parse(request)
        try:
            user = User.objects.get(nick_name=data['nick_name'])# 输入是用户名
            if user.passwords == data['passwords']:
                request.COOKIES['nick_name'] = user.nick_name
                response = JsonResponse('success',safe=False,status=200)
                response.set_cookie('nick_name',user.nick_name)
                return response
            else:
                return error('用户名密码不匹配')# 返回206
        except:
            try:
                user = User.objects.get(student_id=data['nick_name'])# 如果输入的是学号
                if user.passwords == data['passwords']:
                    request.COOKIES['nick_name'] = user.nick_name
                    return success()# 返回200
                else:
                    return error('用户名密码不匹配')  # 返回206
            except:
                return error('error')# 返回400

class Register(APIView):
    def get(self,request):
        return success()
    def post(self,request):
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            try:
                user = User.objects.get(nick_name=data['nick_name'])
                return error('用户名已经被注册')# 返回206
            except:
                try:
                    user = User.objects.get(student_id=data['student_id'])# 学号已经被注册
                    return error('学号已经被注册')# 返回206
                except:
                    serializer.save()
                    return success()
        return error('error')# 表单验证失败返回400

