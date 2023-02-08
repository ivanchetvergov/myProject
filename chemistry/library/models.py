from django.db import models

class Articles(models.Model):
    shorts = models.CharField('Название', max_length=250,default='Блок Задание ')
    full = models.TextField('Описание')
    decision = models.TextField('Решение', default='Решение: ')
    answer = models.CharField('Ответ', max_length=250, default='Ответ: ')
    key = models.CharField('Ключ', max_length=250, default=1)

    def __str__(self):
        return self.shorts

    def get_absolute_url(self):
        return f'/library/{self.id}'

    class Meta:
        verbose_name = 'библиотека'
        verbose_name_plural = 'Библиотека'

class Blog(models.Model):
    title = models.CharField(max_length=255, unique=True)
    body = models.TextField()

    def __str__(self):
        return self.title




