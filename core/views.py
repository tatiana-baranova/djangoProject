from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h3>Hello</h3>')


def services(request):
    return HttpResponse('<h3>How are you</h3>')
