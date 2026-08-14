from django.shortcuts import render
from .models import News
def home(request):
    data = {
        'title': 'Головна сторінка'
    }

    return render(request, 'core/home.html', data)


def services(request):
    data = {
        'news': News.objects.all(),
        'title': 'Послуги'
    }

    return render(request, 'core/services.html', data)