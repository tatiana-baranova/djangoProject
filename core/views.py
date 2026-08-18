from django.shortcuts import render
from .models import News
from django.views.generic import ListView

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

class ShowNewsView(ListView):
    model = News
    template_name = 'core/articles.html'
    context_object_name = 'news'
    ordering = ['-date']


    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = 'Сторінка з статтями'
        return ctx