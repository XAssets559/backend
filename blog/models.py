from django.db import models
from user.models import User
import uuid

# Create your models here.

class Article(models.Model):
    '''
    blog文章：标题;描述;内容;作者;点赞数;创建时间
    '''
    id =  models.UUIDField(primary_key = True , auto_created = True , default = uuid.uuid1, editable = False )
    title = models.CharField(max_length=100)#文章的标题
    des = models.TextField()#文章的描述，用来显示的
    context = models.TextField()
    author = models.ForeignKey(to=User,default=None,on_delete=models.CASCADE,related_name='article')
    zan_num = models.IntegerField(default=0)#点赞数
    c_time = models.DateTimeField(auto_now=True)