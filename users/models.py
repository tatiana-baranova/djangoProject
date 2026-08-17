from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import os
class Profile(models.Model):
    user = models.OneToOneField(User,verbose_name='Користувач', on_delete=models.CASCADE)
    img = models.ImageField('Фото користувача', default='default.png', upload_to='user_images')

    def __str__(self):
        return f'Профіль користувача {self.user.username}'

    def save(self, *args, **kwargs):
        old = Profile.objects.get(pk=self.pk)
        if old.img and old.img != self.img:
            if old.img.name != 'default.png' and os.path.isfile(old.img.path):
                os.remove(old.img.path)

        super().save()
        image = Image.open(self.img.path)
        if image.height > 256 or image.width > 256:
            resize = (256, 256)
            image.thumbnail(resize)
            image.save(self.img.path)

    class Meta:
        verbose_name = 'Профіль'
        verbose_name_plural = 'Профіль'