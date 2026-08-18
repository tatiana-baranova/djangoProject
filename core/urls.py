from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('uslugi', views.services, name='services'),
    path('articles', views.ShowNewsView.as_view(), name='articles'),
]