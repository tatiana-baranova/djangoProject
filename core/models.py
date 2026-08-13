from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
class News(models.Model):
    title = models.CharField('Назва статті', max_length=100)
    text = models.TextField('Основний текст статті')
    date = models.DateTimeField('Дата опублікування', default=timezone.now)
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'
    class Meta:
        verbose_name = 'Новина'
        verbose_name_plural = 'Новини'
