from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="home"),
    path('projects/',views.projects_view, name="projects"),
    path('web/',views.web_view, name="web"),
    path('iot/',views.iot_view, name="iot"),
    path('sent/',views.send_view, name="sent"),
    path('success/', views.successView, name='success'),

]
