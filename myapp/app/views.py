from django.shortcuts import render
from django.http import HttpResponse
from app.models import Bio

def home(request):
    key =Bio.objects.all()
    return render(request,"sample.html",{"data":key})
def Index(request):
    return render(request,"index.html",{})

def Index2(request):
    return render(request,"index2.html",{})

# Create your views here.
def temp(request):
    return render(request,"temp.html",{})