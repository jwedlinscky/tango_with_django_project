from django.contrib import admin
from django.urls import path
from django.urls import include
from django.shortcuts import render
from django.http import HttpResponse

from rango import views
from rango.models import Category


def index(request):
    # Query the database for a list of ALL categories currently stored.
    # Order the categories by the number of likes in descending order.
    # Retrieve the top 5 only -- or all if less than 5.
    # Place the list in our context_dict dictionary (with our boldmessage!)
    # that will be passed to the template engine.
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    # Render the response and send it back!
    return render(request, 'rango/index.html', context=context_dict)


urlpatterns = [
path('', views.index, name='index'),
path('rango/', include('rango.urls')),
# The above maps any URLs starting with rango/ to be handled by rango.
path('admin/', admin.site.urls),
]
