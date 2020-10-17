# -*- coding: utf-8 -*-
# @Time    : 2020/10/16 10:06
# @Author  : Mr.Xia
# @FileName: serializers.py
# @Software: PyCharm

from rest_framework import serializers
from .models import *

class ArticleDetialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id','title','des','context','author','c_time']

class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id','title','des','author']