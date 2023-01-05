from django.db import models
from django.urls import reverse
from .utils import CustomStr


class Movies(CustomStr, models.Model):
    title = models.CharField(max_length=150, verbose_name="Наименование")
    content = models.TextField(blank=True, verbose_name="Описание")
    created_at = models.DateField(auto_now_add=True, verbose_name="Создан")
    updated_at = models.DateField(auto_now=True, verbose_name="Изменен")
    photo = models.ImageField(upload_to='photos/movies_thumb/%Y/%m/%d/', verbose_name="Фото", blank=True)
    is_published = models.BooleanField(default=True, verbose_name="Опубликован")
    default_rate = models.FloatField(blank=True, default=None, null=True, verbose_name="Рейтинг по умолчанию")
    age = models.IntegerField(blank=True, default=None, null=True, verbose_name="Возраст")
    country = models.CharField(max_length=150, blank=True, verbose_name="Страна")
    year = models.IntegerField(blank=True, default=None, null=True, verbose_name="Год")
    genre = models.CharField(max_length=150, blank=True, verbose_name="Жанр")
    director = models.CharField(max_length=150, blank=True, verbose_name="Режисер")
    time = models.TimeField(blank=True, default=None, null=True, verbose_name="Время")
    actors = models.CharField(max_length=150, blank=True, verbose_name="Актеры")
    related = models.TextField(blank=True, verbose_name="Похожие")
    trailer = models.TextField(blank=True, verbose_name="Трейлер")
    serial = models.BooleanField(default=False, verbose_name="Сериал")
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, blank=True, verbose_name="Категория")
    tags = models.ManyToManyField('Tags', blank=True, verbose_name="Теги")
    views = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('view_movie', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
        ordering = ['-created_at', 'title']


class Category(CustomStr, models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']


class Tags(CustomStr, models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование тега')

    def get_absolute_url(self):
        return reverse('tag', kwargs={'tag_id': self.pk})

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['title']

