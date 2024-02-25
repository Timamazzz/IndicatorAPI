from django.contrib import admin

from .models import RunningLine, RunningText, Contact, ContactsLink, CustomerLink, Requisite
from modeltranslation.admin import TranslationAdmin, TranslationInlineModelAdmin, TranslationTabularInline


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
class RequisiteAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'certificate', 'inn', 'ogrnip', 'checking_account', 'bik', 'bank', 'correspondent_account', 'is_active')
