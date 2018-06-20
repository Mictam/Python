from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

# Create your views here.
def home(request):
    return render(request,'home/index.html',context)