from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('pet/', views.pet),

    path('calendar/', views.calendar),
    path('calendar/record/', views.calendar_record),
    
    path('room/', views.calendar),
    path('room/visit/', views.calendar),
]