from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse,HttpResponse
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.db.models import Count
from database.models import DailyAnalytics,TaskList
import datetime

def boss(request):
    domain = request.META.get('HTTP_HOST')
    return redirect(f'https://{domain}/admin')

@login_required(login_url=reverse_lazy('boss'))
def home(request):
    waked_up = 0
    done_gym = 0
    done_noti = 0
    done_post = 0
    done_yt = 0
    today = datetime.date.today().strftime('%Y-%m-%d')
    data = DailyAnalytics.objects.filter(date=today)
    
    if request.method == 'POST':
        if request.POST.get('woke_up') == 'done':
            new_day = DailyAnalytics()
            new_day.save()
            
        if request.POST.get('slept') == 'done':
            try:
                today_data = DailyAnalytics.objects.get(date=today)
                today_data.slept = datetime.datetime.now()
                today_data.save()
            except:
                pass
            
        if request.POST.get('task'):
            new_task = TaskList(task = request.POST.get('task'))
            new_task.save()
            
    if len(data) > 0:
        waked_up = 1
        if data[0].gym == True:
            done_gym = 1
        if data[0].bh_post == True:
            done_post = 1
        if data[0].bh_noti == True:
            done_noti = 1
        if data[0].yt == True:
            done_yt = 1
            
    all_task = TaskList.objects.all()
        
        
    response = {
        'waked_up':waked_up,
        'done_gym':done_gym,
        'done_post':done_post,
        'done_noti':done_noti,
        'done_yt':done_yt,
        'all_task':all_task,
    }
    return render(request,'home.html',response)

def complete_task(request,id):
    try:
        task_data = TaskList.objects.get(id=id)
        task_data.completed = True
        task_data.save()
        return redirect('home')
        
    except:
        return redirect('home')
    

def done_gym(request):
    try:
        today = datetime.date.today().strftime('%Y-%m-%d')
        data = DailyAnalytics.objects.filter(date=today)
        data_obg = DailyAnalytics.objects.get(date=today)
        if len(data) > 0:
            data_obg.gym = True
            data_obg.save()
        return redirect('home')
    except:
        return redirect('home')

def done_noti(request):
    try:
        today = datetime.date.today().strftime('%Y-%m-%d')
        data = DailyAnalytics.objects.filter(date=today)
        data_obg = DailyAnalytics.objects.get(date=today)
        if len(data) > 0:
            data_obg.bh_noti = True
            data_obg.save()
        return redirect('home')
    except:
        return redirect('home')

def done_post(request):
    try:
        today = datetime.date.today().strftime('%Y-%m-%d')
        data = DailyAnalytics.objects.filter(date=today)
        data_obg = DailyAnalytics.objects.get(date=today)
        if len(data) > 0:
            data_obg.bh_post = True
            data_obg.save()
        return redirect('home')
    except:
        return redirect('home')
    
def done_yt(request):
    try:
        today = datetime.date.today().strftime('%Y-%m-%d')
        data = DailyAnalytics.objects.filter(date=today)
        data_obg = DailyAnalytics.objects.get(date=today)
        if len(data) > 0:
            data_obg.yt = True
            data_obg.save()
        return redirect('home')
    except:
        return redirect('home')
    
    