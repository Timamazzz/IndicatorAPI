from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from modelcluster.fields import ParentalManyToManyField, ParentalKey
from wagtail import blocks
from wagtail.admin.panels import MultiFieldPanel, FieldPanel
from wagtail.api import APIField
from wagtail.blocks import ListBlock, BlockQuoteBlock
from wagtail.fields import StreamField
from wagtail.models import Page

from project_app_v2.block import LinkBlock
from project_app_v2.fields import ImageChooserBlockField, RichTextFieldBlock, DocumentChooserBlockField
from projects_app.models import Tag
from django.utils.translation import gettext_lazy as _

from wagtail.api.v2.serializers import StreamField as StreamFieldSerializer, BaseSerializer

from django import forms

# Create your models here.

class TagSerializer(BaseSerializer):
    meta_fields = []

    class Meta:
        fields = '__all__'
        model = Tag


class ProjectPage(Page):
    header_html = models.TextField(blank=True, null=True, verbose_name=_('Название компонента'))

    header_file = models.FileField(upload_to='projects/headers/', blank=True, null=True,
                                   verbose_name=_('Файл превью'))

    description = models.TextField(verbose_name=_('Описание'), null=True, blank=True)

    is_light_background_header = models.BooleanField(default=False, verbose_name=_('Светлый фон'))
    column = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(3)],
                                         verbose_name=_("Ширина в колонках"))
    tags = ParentalManyToManyField(Tag, blank=True, related_name='projects_v2', verbose_name=_('Метки'))
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    date = models.DateField(verbose_name=_('Дата'), null=True, blank=True)

    content = StreamField(
        block_types=(
            ('heading', blocks.CharBlock(form_classname="title")),
            ('image', ImageChooserBlockField()),
            ('slider', ListBlock(ImageChooserBlockField())),
            ('gallery', ListBlock(ImageChooserBlockField())),
            ('paragraph', RichTextFieldBlock()),
            ('documents', ListBlock(DocumentChooserBlockField())),
            ('quote', BlockQuoteBlock()),
            ('link', LinkBlock()),
        ), verbose_name=_("Контент сайта")
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel("header_html"), FieldPanel('is_light_background_header'),
            FieldPanel('column'), FieldPanel('tags'), FieldPanel('order'), FieldPanel('description'),
            FieldPanel('header_file'), FieldPanel('date')
        ], heading="Базовые настройки страницы"),
        FieldPanel('content')
    ]

    api_fields = [
        APIField('title'), APIField('slug'),
        APIField('header_html'), APIField('is_light_background_header'), APIField('description'),
        APIField('header_file'),
        APIField('column'), APIField('tags', serializer=TagSerializer(many=True)), APIField('order'),
        APIField('content', serializer=StreamFieldSerializer()),

    ]

    def get_views(self):
        return UniqueProjectViewPage.objects.filter(project=self).count()

    class Meta:
        ordering = ('order',)


class UniqueProjectViewPage(models.Model):
    project = ParentalKey(ProjectPage, on_delete=models.CASCADE)
    ip_address = models.CharField(max_length=45)
    user_agent = models.CharField(max_length=255)
    viewed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('project', 'ip_address', 'user_agent')
