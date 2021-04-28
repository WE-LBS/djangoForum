from django.shortcuts import render
from django.utils import timezone

def index(request):
    context = {

    }
    return render(request,'sub/index.html',context)

def login(request):
    context={

    }
    return render(request,'sub/login.html',context)