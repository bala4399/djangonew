from django.shortcuts import render
from django.http import HttpResponse


def Index(request):
    return render(request,"index.html",{})

def Index2(request):
    return render(request,"index2.html",{})

# Create your views here.
