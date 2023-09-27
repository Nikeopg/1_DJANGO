from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse

# Create your views here.

def redirect_to_figure(request, **kwargs):
    path = request.path
    figure = path.split("/")[2]

    if figure == 'get_rectangle_area':
        redirected_url = reverse("rectangle", kwargs={"width": kwargs["width"], "height": kwargs["height"]})
        return HttpResponseRedirect(redirected_url)
    elif figure == 'get_square_area':
        redirected_url = reverse("square", kwargs={"width": kwargs["side"]})
        return HttpResponseRedirect(redirected_url)
    elif figure == 'get_circle_area':
        redirected_url = reverse("circle", kwargs={"radius": kwargs["radius"]})
        return HttpResponseRedirect(redirected_url)
    else:
        return HttpResponseNotFound('bad figure')


def get_rectangle(request,width: int, height: int):
    return HttpResponseRedirect(f'/calculate_geometry/rectangle/{width}/{height}/')

def rect_area(request, width, height):
    return HttpResponse(f"Площадь прямоугольнечга {width}x{height} = {width*height}")

def square_area(request, width):
    return HttpResponse(f"Площадь квадрата {width}x{width}, но не квадракоптера = {width**2}")

def circle_area(request, radius):
    return HttpResponse(f"Площадь круга радиусом как твой болт {radius} = {radius*3.14}")