from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

dic_week_day = {'monday': 'Понедельник!',
                'tuesday': 'Вторник!',
                'wednesday': 'Среда!',
                'thursday': 'Четверг!',
                'friday': 'Пятница!',
                'saturday': 'Суббота!',
                'sunday': 'Воскресенье!',}


def day(request,day: str):
    return HttpResponse(f"А это день денечек: {dic_week_day[day]}")

def day_number(request, day: int):
    list_week_days = list(dic_week_day)
    if day > len(dic_week_day):
        return HttpResponseNotFound(f"Бро, такого дня {day} как бэ неть!")
    this_day = list_week_days[day-1]
    redirected_url = reverse("todo_week-name", args = {this_day, })
    return HttpResponseRedirect(redirected_url)


