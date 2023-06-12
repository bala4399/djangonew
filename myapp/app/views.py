from django.shortcuts import render
from django.http import HttpResponse

def Index(request):
    return HttpResponse("hello world")

# Create your views here.
