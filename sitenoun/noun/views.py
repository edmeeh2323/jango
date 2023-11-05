from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    #t = reverse('about/')
    #print(t)
    #return redirect(t)
    return HttpResponse("Страница приложения noun.")


def about(request):
    return HttpResponse("Страница приложения ab.")




# def year_archive(request, year):
# return HttpResponse(f"<h1>Архив по годам.</h1><p>{year}</p>")

def categories(request, cat_id):
    return HttpResponse(f"<h1>Статьи по категориям.</h1><p>id: {cat_id}</p>")


def categories_by_slug(request, cat_slug):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>Статьи по категориям.</h1><p>slug: {cat_slug}</p>")


def archive(request, year):
    if year > 2023:
        return HttpResponseRedirect('home')
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
