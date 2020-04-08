from django.urls import path, re_path
from django.conf.urls import url
from . import views

urlpatterns = [
    re_path(r'^/(?P<stream_path>(.*?))/$', views.dynamic_stream,name="videostream"),  
    path('',views.index, name='index'),
    path('showStats/', views.showStats, name="showStats"),
    path('startWorkout/', views.startWorkout, name="startWorkout"),
    path('stopWorkout/', views.stopWorkout, name="stopWorkout"),
    path('showWorkout/', views.showWorkout, name="showWorkout"),
    path('playSound/', views.playSound, name="playSound")
]