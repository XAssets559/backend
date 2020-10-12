from django.shortcuts import render
from .serializers import *
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

# Create your views here.

@csrf_exempt
def login(request):
    message = 'faild'
    if request.method == 'GET':
        return JsonResponse('hello',safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        try:
            user = User.objects.get(nick_name=data['nick_name'])
            if user.passwords == data['passwords']:
                message = 'success'
        except:
            try:
                user = User.objects.get(student_id = data['nick_name'])
                if user.passwords == data['passwords']:
                    message = 'success'
            except:
                pass
        return JsonResponse(message,safe=False)

@csrf_exempt
def register(request):
    if request.method == 'GET':
        return JsonResponse('hello',safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            try:
                user = User.objects.get(nick_name=data['nick_name'])
                message = 'This name has already registered'
            except:
                serializer.save()
                message = 'success'
        return JsonResponse(message,safe=False)