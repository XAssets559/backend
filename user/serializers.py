# -*- coding: utf-8 -*-
# @Time    : 2020/10/10 22:39
# @Author  : Mr.Xia
# @FileName: serializers.py
# @Software: PyCharm

from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['nick_name','passwords','status','student_id','email']



class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title','descriptions','demo_scripts']

class ScriptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scripts
        fields = ['context','submit_time']