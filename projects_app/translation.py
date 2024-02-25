# translation.py
from modeltranslation.translator import TranslationOptions, translator
from .models import Tag, Project, Content


class TagTranslationOptions(TranslationOptions):
    fields = ('name',)


class ProjectTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


class ContentTranslationOptions(TranslationOptions):
    fields = ('text', 'url_name', 'file_name')


translator.register(Tag, TagTranslationOptions)
translator.register(Project, ProjectTranslationOptions)
translator.register(Content, ContentTranslationOptions)
