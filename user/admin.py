from django.contrib import admin
from .models import *

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('nick_name','student_id','passwords','grades','status')

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('nick_name','passwords')

class ScriptsAdmin(admin.ModelAdmin):
    list_display = ('id','title','submit_time','context',)

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title','c_time')

admin.site.register(User,UserAdmin)
admin.site.register(Scripts,ScriptsAdmin)
admin.site.register(Task,TaskAdmin)
