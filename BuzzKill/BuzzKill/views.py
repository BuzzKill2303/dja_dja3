# python manage.py runserver
from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    return render(request,'about.html',{'grey':4})


def home(request):
    return HttpResponse('This is my home')