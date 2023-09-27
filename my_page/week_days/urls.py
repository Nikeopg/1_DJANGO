from django.urls import path
from . import views

urlpatterns = [
    path('<int:day>/', views.day_number),
    path('<str:day>/', views.day, name = "todo_week-name"),
    ]