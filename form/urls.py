from unicodedata import name
from django.contrib import admin
from django.urls import path
from formapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.addform, name='home'),
    path('thanks/', views.thanks, name='thanks'),
    path('about/', views.about, name='about-us'),
    path('sport/', views.sport, name='sport'),
    path('politics/', views.politics, name='politics'),
    # path('evenodd/', views.evenoddNumber, name='evenodd'),
    # path('calculator/', views.calculator, name='calc'),
    # path('marksheet/', views.marksheet, name='marksheet'),
]
