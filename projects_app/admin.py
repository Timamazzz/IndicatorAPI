from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationInlineModelAdmin

from adminsortable.admin import SortableTabularInline, SortableStackedInline, SortableAdminMixin
from .models import Project, Content, Gallery, GalleryImage, Tag
from django.db import models
from ckeditor.widgets import CKEditorWidget


class GalleryImageInline(SortableTabularInline):
    model = GalleryImage
    extra = 1


@admin.register(Gallery)
class GalleryAdmin(SortableAdminMixin, admin.ModelAdmin):
    inlines = [GalleryImageInline]
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget(config_name='default')}
    }


class ContentInline(SortableStackedInline, TranslationInlineModelAdmin):
    model = Content
    extra = 1
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget(config_name='default')}
    }


@admin.register(Project)
class ProjectAdmin(SortableAdminMixin, TranslationAdmin):
    inlines = [ContentInline]
    list_display = ['title', 'description', 'order']
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget(config_name='default')}
    }
    exclude_ckeditor_fields = ['header_html', 'description']

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in ['header_html', 'description']:
            kwargs['widget'] = admin.widgets.AdminTextInputWidget()
        return super(ProjectAdmin, self).formfield_for_dbfield(db_field, **kwargs)


@admin.register(Tag)
class TagAdmin(TranslationAdmin):
    list_display = ['name', ]
