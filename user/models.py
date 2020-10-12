from django.db import models
import uuid
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

status_chioces = (
    (1,'老师'),
    (0,'学生')
)
class User(models.Model):
    id =  models.UUIDField(primary_key = True , auto_created = True , default = uuid.uuid1, editable = False )
    nick_name = models.CharField(max_length=20)
    student_id = models.CharField(max_length=10,blank=True,null=True)
    passwords = models.CharField(max_length=20)
    email = models.EmailField()
    grades = models.FloatField(max_length=4,null=True,blank = True,validators=[MinValueValidator(0.0), MaxValueValidator(60.0)]) #满分60(分数区间[0.0-60.0])
    status = models.IntegerField(default=0,choices=status_chioces)



class Scripts(models.Model):
    submit_time = models.DateTimeField(auto_now=True,editable=False)
    context = models.TextField()
    to_user = models.ForeignKey(to=User,default=None,on_delete=models.CASCADE,related_name='scripts')
    title = models.CharField(max_length=20)

class Task(models.Model):
    title = models.CharField(max_length=20)
    descriptions = models.TextField()
    demo_scripts = models.TextField()
    c_time = models.DateField(auto_now=True, editable=False)
    to_user = models.ForeignKey(to=User,default=None,on_delete=models.CASCADE,related_name='task')
