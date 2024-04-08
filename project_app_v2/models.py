from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
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

from wagtail.api.v2.serializers import StreamField as StreamFieldSerializer


# Create your models here.

class ProjectPage(Page):
    header_html = models.TextField(blank=True, null=True, verbose_name=_('Название компонента'))

    header_file = models.FileField(upload_to='projects/headers/', blank=True, null=True,
                                   verbose_name=_('Файл превью'))

    description = models.TextField(verbose_name=_('Описание'), null=True,blank=True)

    is_light_background_header = models.BooleanField(default=False, verbose_name=_('Светлый фон'))
    column = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(3)],
                                         verbose_name=_("Ширина в колонках"))
    tags = models.ManyToManyField(Tag, blank=True, related_name='projects_v2', verbose_name=_('Метки'))
    order = models.PositiveIntegerField(default=0, blank=False, null=False)


    content = StreamField(
        block_types=(
            ('heading', blocks.CharBlock(form_classname="title")),
            ('image', ImageChooserBlockField()),
            ('slider', ListBlock(ImageChooserBlockField())),
            ('gallery', ListBlock(ImageChooserBlockField())),
            ('paragraph', RichTextFieldBlock()),
            ('documents', ListBlock(DocumentChooserBlockField())),
            ('quote', BlockQuoteBlock()),
            ('link', LinkBlock())
        ), verbose_name=_("Контент сайта")
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel("header_html"), FieldPanel('is_light_background_header'),
            FieldPanel('column'), FieldPanel('tags'), FieldPanel('order')
        ], heading="Базовые настройки страницы"),
        FieldPanel('content')
    ]

    api_fields = [
        APIField('slug'),
        APIField('header_html'), APIField('is_light_background_header'),
        APIField('column'), APIField('tags'), APIField('order'), APIField('content', serializer=StreamFieldSerializer()),

    ]

    class Meta:
        ordering = ('order',)
