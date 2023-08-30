from django.db import models
from django.utils import timezone

# Create your models here.
class DailyAnalytics(models.Model):
    date = models.DateField(default=timezone.now)
    woke_up = models.DateTimeField(default=timezone.now)
    slept = models.DateTimeField(null=True)
    gym = models.BooleanField(default=False)
    bh_noti = models.BooleanField(default=False)
    bh_post = models.BooleanField(default=False)
    yt = models.BooleanField(default=False)
    
class TaskList(models.Model):
    task = models.CharField(max_length=255)
    created = models.DateTimeField(default=timezone.now)
    completed =  models.BooleanField(default=False)
    
    