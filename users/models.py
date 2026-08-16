from django.db import models
from django.contrib.auth.models import User
class Profile(models.Model):
    user = models.OneToOneField(User,verbose_name='Користувач', on_delete=models.CASCADE)
    img = models.ImageField('Фото користувача', default='default.png', upload_to='user_images')

    def __str__(self):
        return f'Профіль користувача {self.user.username}'

    class Meta:
        verbose_name = 'Профіль'
        verbose_name_plural = 'Профіль'