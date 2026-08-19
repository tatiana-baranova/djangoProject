from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
class News(models.Model):
    title = models.CharField('Назва статті', max_length=100, unique=True)
    text = models.TextField('Основний текст статті')
    date = models.DateTimeField('Дата опублікування', default=timezone.now)
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)

    views = models.IntegerField('Перегляди', default=1)

    # sizes = (
    #     ('S', 'Small'),
    #     ('M', 'Medium'),
    #     ('L', 'Large'),
    #     ('XL', 'X Large'),
    # )
    # shop_sizes = models.CharField(choices=sizes, max_length=2, default='S')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("news_detail", kwargs={"pk": self.pk})
    
    class Meta:
        verbose_name = 'Новина'
        verbose_name_plural = 'Новини'


class ContactMessage(models.Model):
    subject = models.CharField('Тема листа',max_length=200)
    email = models.EmailField('Електрона адреса')
    message = models.TextField('Текст повідомлення')
    created_at = models.DateTimeField('Дата відправлення', auto_now_add=True)

    def __str__(self):
        return self.subject