from django.contrib import admin
from .models import TaskList,DailyAnalytics

# Register your models here.

class AdminDailyAnalytics(admin.ModelAdmin):
    list_display = ['date','woke_up','slept','gym','bh_noti','bh_post']
admin.site.register(DailyAnalytics,AdminDailyAnalytics)

class AdminTaskList(admin.ModelAdmin):
    list_display = ['task','created','completed']
admin.site.register(TaskList,AdminTaskList)
