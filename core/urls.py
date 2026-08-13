from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('uslugi', views.services),
]