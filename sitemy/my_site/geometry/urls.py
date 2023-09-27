from django.urls import path
from . import views

urlpatterns = [
    path('rectangle/<int:width>/<int:height>/', views.rect_area, name="rectangle"),
    path('square/<int:width>/', views.square_area, name="square"),
    path('circle/<int:radius>/', views.circle_area, name="circle"),

    path('get_square_area/<int:side>/', views.redirect_to_figure),
    path('get_circle_area/<int:radius>/', views.redirect_to_figure),
    path('get_rectangle_area/<int:width>/<int:height>/', views.redirect_to_figure),
    ]