from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('uploads/simple/', views.simple_upload, name='simple_upload'),
    path('index/', views.index, name='index'),


    
]
