from django.urls import path

from . import views

urlpatterns = [
    path('new',views.Index3,name="Index3"),
    path("register",views.Register,name="Register"),
    path('',views.temp,name="temp"),
]