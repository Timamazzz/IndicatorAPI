from django.contrib import admin
from adminsortable.admin import SortableTabularInline, SortableStackedInline, SortableAdminMixin
from .models import Project, Content, Gallery, GalleryImage


class GalleryImageInline(SortableTabularInline):
    model = GalleryImage
    extra = 1


@admin.register(Gallery)
class GalleryAdmin(SortableAdminMixin, admin.ModelAdmin):
    inlines = [GalleryImageInline]


class ContentInline(SortableStackedInline):
    model = Content
    extra = 1


@admin.register(Project)
class ProjectAdmin(SortableAdminMixin, admin.ModelAdmin):
    inlines = [ContentInline]
    list_display = ['title', 'description']
