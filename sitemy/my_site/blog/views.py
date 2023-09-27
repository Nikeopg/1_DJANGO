from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound

# Create your views here.

def main_page(request):
    return HttpResponse("Главная страница получается")

def posts(request):
    return HttpResponse("Все посты блога ТУТ")

def get_post(request, name_post):
    return HttpResponse(f"Пост блога про вот это - {name_post}")

def post_number(request, number_post : int):
    return HttpResponse(f"Здесь содержится информация о посте под номером {number_post}")