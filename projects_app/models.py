from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')

    header_file = models.FileField(upload_to='projects/headers/', blank=True, null=True, verbose_name='Файл заголовка')
    header_html = models.TextField(blank=True, null=True, verbose_name='HTML заголовка')

    description = models.TextField(verbose_name='Описание')

    url = models.URLField(blank=True, null=True, verbose_name='Ссылка')

    date = models.DateField(verbose_name='Дата')

    column = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(3)], verbose_name="Колонка отображения на главной")
    order = models.PositiveIntegerField(default=0, blank=False, null=False, )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        ordering = ['order']
        app_label = 'projects_app'


class Gallery(models.Model):
    TILE = 'tile'
    SLIDER = 'slider'

    GALLERY_TYPE_CHOICES = [
        (TILE, 'Плитка'),
        (SLIDER, 'Слайдер'),
    ]

    type = models.CharField(max_length=20, choices=GALLERY_TYPE_CHOICES, default=TILE, verbose_name='Тип галереи')
    order = models.PositiveIntegerField(default=0, blank=False, null=False, )

    def __str__(self):
        return f'Gallery for Content {self.id}'

    class Meta:
        verbose_name = 'Галлерея'
        verbose_name_plural = 'Галлереи'
        ordering = ['order']
        app_label = 'projects_app'


class GalleryImage(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, related_name='images', verbose_name='Галерея')
    file = models.FileField(upload_to='projects/gallery_images/', verbose_name='Изображение')
    order = models.PositiveIntegerField(default=0, blank=False, null=False, )

    def __str__(self):
        return f'Image {self.id} in Gallery {self.gallery.id}'

    class Meta:
        verbose_name = 'Изображение галлереи'
        verbose_name_plural = 'Изображения галлереи'
        ordering = ['order']
        app_label = 'projects_app'


class Content(models.Model):
    TEXT = 'text'
    URL = 'url'
    FILE = 'file'
    Image = 'image'
    GALLERY = 'gallery'

    CONTENT_TYPE_CHOICES = [
        (TEXT, 'Текст'),
        (URL, 'URL'),
        (FILE, 'Файл'),
        (Image, 'Изображение'),
        (GALLERY, 'Галерея')
    ]

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='contents')
    content_type = models.CharField(max_length=20, choices=CONTENT_TYPE_CHOICES, default=TEXT,
                                    verbose_name='Тип контента')

    text = models.TextField(blank=True, null=True, verbose_name='Текст')

    url = models.URLField(blank=True, null=True, verbose_name='URL')
    url_name = models.CharField(max_length=1024, blank=True, null=True, verbose_name='Отображаемое имя ссылки')

    file = models.FileField(upload_to='projects/files/', null=True, blank=True, verbose_name='Файл')
    file_name = models.CharField(max_length=1024, blank=True, null=True, verbose_name='Отображаемое имя файла')

    image = models.FileField(upload_to='projects/images/', null=True, blank=True, verbose_name='Изображение')

    gallery = models.ForeignKey(Gallery, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Галлерея')

    order = models.PositiveIntegerField(default=0, blank=False, null=False, )

    def __str__(self):
        return f'Content {self.id} for {self.project.title}'

    class Meta:
        verbose_name = 'Контент'
        verbose_name_plural = 'Контент'
        ordering = ['order']
        app_label = 'projects_app'
