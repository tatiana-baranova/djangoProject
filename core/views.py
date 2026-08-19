from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import News, ContactMessage
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView,
    DeleteView,
    FormView
    )
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.mail import send_mail
from django.contrib import messages
from django.urls import reverse_lazy

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
    paginate_by = 4

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = 'Сторінка з статтями'
        return ctx


class UserAllNewsView(ListView): 
    model = News
    template_name = 'core/user_news.html'
    context_object_name = 'news'
    paginate_by = 5

    def get_queryset(self):
            user = get_object_or_404(User, username=self.kwargs['username'])
            return News.objects.filter(author=user).order_by('-date')
    
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = f'Статті користувача: {self.kwargs.get('username')}'

        return ctx 

class NewsDetailView(DetailView):
    model = News
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
            ctx = super().get_context_data(**kwargs)

            ctx['title'] = News.objects.get(pk=self.kwargs['pk'])

            return ctx


class CreateNewsView(LoginRequiredMixin, CreateView):
    model = News
    template_name = 'core/create_news.html'

    fields = ['title', 'text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        
        ctx['title'] = 'Додавання статті'
        ctx['btn_title'] = 'Додати'
        
        return ctx


class UpdateNewsView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = News
    template_name = 'core/create_news.html'
    
    fields = ['title', 'text']

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.author:
            return True
        return False
    
    def form_valid(self, form):
            form.instance.author = self.request.user
            return super().form_valid(form)

    def get_context_data(self, **kwargs):
                ctx = super().get_context_data(**kwargs)
    
                ctx['title'] = 'Оновлення статті'
                ctx['btn_title'] = 'Оновить статтю'
    
                return ctx


class DeleteNewsView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = News
    template_name = 'core/delete_news.html'
    success_url = '/'

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.author:
            return True
        return False


class ContactView(CreateView):
    model = ContactMessage
    template_name = 'core/contacts.html'
    success_url = reverse_lazy('profile')
    fields = ['subject', 'email', 'message']

    def form_valid(self, form):
        contact = form.save()

        send_mail(
            subject=contact.subject,
            message=contact.message,
            from_email=contact.email,
            recipient_list=['tetiana.baranova18@gmail.com'],
        )
        messages.success(
            self.request,
            'Повідомлення успішно відправлено!'
        )
        return super().form_valid(form)
    