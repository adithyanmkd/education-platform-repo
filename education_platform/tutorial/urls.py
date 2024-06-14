from django.urls import path
from . import views

urlpatterns = [
    path('', views.tutorial, name='tutorial'),
    path('playlist/', views.playlist, name='playlist'),
    
]