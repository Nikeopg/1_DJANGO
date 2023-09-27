from django.urls import path
from . import views

urlpatterns = [
    path('<int:number_post>', views.post_number),
    path('<name_post>', views.get_post),
    path('', views.posts),
]