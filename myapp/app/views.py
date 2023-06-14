from django.shortcuts import redirect, render
from django.http import HttpResponse
from app.models import Bio
from django.contrib.auth.forms import UserCreationForm

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

def Index3(request):
    return render(request,"index3.html",{})

def Register(request):
    if request.method == "POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Index3")
    else:
        form=UserCreationForm()
    return render(request,"registration/register.html",{"form":form})