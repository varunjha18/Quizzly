from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
   path('', views.home, name='home'),
   path('<int:quiz_id>/start_quiz',views.start_quiz,name='start_quiz'),
   path('<int:quiz_id>',views.question,name='question'),
]