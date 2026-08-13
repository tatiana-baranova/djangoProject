from django.shortcuts import render

def home(request):
    data = {
        'title': 'Головна сторінка'
    }

    return render(request, 'core/home.html', data)


def services(request):
    return render(request, 'core/services.html', {'title': 'Послуги'})