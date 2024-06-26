from django.contrib import admin

from .models import RunningLine, RunningText, Contact, ContactsLink, CustomerLink, Requisite, PrivacyPolicy
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from django.db import models
from ckeditor.widgets import CKEditorWidget


class RunningTextInline(TranslationTabularInline):
    model = RunningText


class ContactsLinkInline(TranslationTabularInline):
    model = ContactsLink


class CustomerLinkInline(TranslationTabularInline):
    model = CustomerLink


@admin.register(RunningLine)
class RunningLineAdmin(TranslationAdmin):
    inlines = [RunningTextInline]
    list_display = ('name', 'is_active')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    inlines = [ContactsLinkInline]
    list_display = ('phone', 'email')


@admin.register(Requisite)
class RequisiteAdmin(TranslationAdmin):
    list_display = (
        'name', 'certificate', 'inn', 'ogrnip', 'checking_account', 'bik', 'bank', 'correspondent_account', 'is_active')


@admin.register(CustomerLink)
class CustomerLinkAdmin(TranslationAdmin):
    list_display = ('name', 'url')


@admin.register(PrivacyPolicy)
class PrivacyPolicyAdmin(TranslationAdmin):
    list_display = ('text',)
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget(config_name='default')}
    }
