from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name = 'home'),
    path('delete/<todo_title>/', views.delete_todo, name = 'delete_todo')

    ]
