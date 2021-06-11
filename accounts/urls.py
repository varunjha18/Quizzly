from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
   path('login', views.login, name='login'),
   path('register', views.register, name='register'),
   path('logout', views.logout, name='logout'),
   path('dashboard', views.dashboard, name='dashboard'),
   path('test_site', views.test_site, name='test_site'),
   path('<str:room_name>/', views.room, name='room'),
  
]