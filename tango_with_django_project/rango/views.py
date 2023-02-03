from django.contrib import admin
from django.urls import path
from django.urls import include
from django.shortcuts import render
from django.http import HttpResponse

from rango import views

def index(request):
    return HttpResponse("Rango says hey there partner!")

urlpatterns = [
path('', views.index, name='index'),
path('rango/', include('rango.urls')),
# The above maps any URLs starting with rango/ to be handled by rango.
path('admin/', admin.site.urls),
]
