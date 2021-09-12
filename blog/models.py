from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time


def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True) #lower + только буквы,цифры и _ -, остльно низя
    return new_slug + '-' + str(int(time()))



class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True) #ставим индексирование для быстрого поиска
    slug = models.SlugField(max_length=150, unique=True, blank=True) #уник. поля по умолчанию индексируются
    body = models.TextField(blank=True, db_index=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
    date_pub = models.DateField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title  #переопредили метод str для отображения

    def save(self, *args, **kwargs):
        if not self.id: # если объекта нет в бд
            self.slug = gen_slug(self.title) #генерация с помощью функции
        super().save(*args, **kwargs)


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title
