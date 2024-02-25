from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name=_('Название'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Метка')
        verbose_name_plural = _('Метки')
        app_label = 'projects_app'


class Project(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('Название'))
    header_file = models.FileField(upload_to='projects/headers/', blank=True, null=True,
                                   verbose_name=_('Файл заголовка'))
    header_html = models.TextField(blank=True, null=True, verbose_name=_('HTML заголовка'))
    description = models.TextField(verbose_name=_('Описание'))
    url = models.URLField(blank=True, null=True, verbose_name=_('Ссылка'))
    date = models.DateField(verbose_name=_('Дата'))
    column = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(3)],
                                         verbose_name=_("Колонка отображения на главной"))
    tags = models.ManyToManyField(Tag, blank=True, related_name='projects', verbose_name=_('Метки'))
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    def __str__(self):
        return self.title

    def get_views_count(self):
        return self.uniqueprojectview_set.count()

    class Meta:
        verbose_name = _('Проект')
        verbose_name_plural = _('Проекты')
        ordering = ['order']
        app_label = 'projects_app'


class UniqueProjectView(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    ip_address = models.CharField(max_length=45)
    user_agent = models.CharField(max_length=255)
    viewed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('project', 'ip_address', 'user_agent')


class Gallery(models.Model):
    TILE = 'tile'
    SLIDER = 'slider'

    GALLERY_TYPE_CHOICES = [
        (TILE, _('Плитка')),
        (SLIDER, _('Слайдер')),
    ]

    type = models.CharField(max_length=20, choices=GALLERY_TYPE_CHOICES, default=TILE, verbose_name=_('Тип галереи'))
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    def __str__(self):
        return _('Галерея для контента {id}').format(id=self.id)

    class Meta:
        verbose_name = _('Галерея')
        verbose_name_plural = _('Галереи')
        ordering = ['order']
        app_label = 'projects_app'


class GalleryImage(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, related_name='images', verbose_name=_('Галерея'))
    file = models.FileField(upload_to='projects/gallery_images/', verbose_name=_('Изображение'))
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    def __str__(self):
        return _('Изображение {id} в галерее {gallery_id}').format(id=self.id, gallery_id=self.gallery.id)

    class Meta:
        verbose_name = _('Изображение галереи')
        verbose_name_plural = _('Изображения галереи')
        ordering = ['order']
        app_label = 'projects_app'


class Content(models.Model):
    TEXT = 'text'
    URL = 'url'
    FILE = 'file'
    Image = 'image'
    GALLERY = 'gallery'

    CONTENT_TYPE_CHOICES = [
        (TEXT, _('Текст')),
        (URL, _('URL')),
        (FILE, _('Файл')),
        (Image, _('Изображение')),
        (GALLERY, _('Галерея')),
    ]

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='contents')
    content_type = models.CharField(max_length=20, choices=CONTENT_TYPE_CHOICES, default=TEXT,
                                    verbose_name=_('Тип контента'))

    text = models.TextField(blank=True, null=True, verbose_name=_('Текст'))

    url = models.URLField(blank=True, null=True, verbose_name=_('URL'))
    url_name = models.CharField(max_length=1024, blank=True, null=True, verbose_name=_('Отображаемое имя ссылки'))

    file = models.FileField(upload_to='projects/files/', null=True, blank=True, verbose_name=_('Файл'))
    file_name = models.CharField(max_length=1024, blank=True, null=True, verbose_name=_('Отображаемое имя файла'))

    image = models.FileField(upload_to='projects/images/', null=True, blank=True, verbose_name=_('Изображение'))

    gallery = models.ForeignKey(Gallery, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_('Галерея'))

    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    def __str__(self):
        return _('Контент {id} для {project_title}').format(id=self.id, project_title=self.project.title)

    class Meta:
        verbose_name = _('Контент')
        verbose_name_plural = _('Контент')
        ordering = ['order']
        app_label = 'projects_app'
