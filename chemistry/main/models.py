from django.db import models

class Massive(models.Model):
    name = models.CharField('Название', max_length=250, default='Урок')
    mean = models.TextField('Описание')
    source = models.CharField('Ключ', max_length=250)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/theory/{self.id}'

    class Meta:
        verbose_name = 'теория'
        verbose_name_plural = 'Теория'