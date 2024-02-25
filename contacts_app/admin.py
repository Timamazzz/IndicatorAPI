from django.contrib import admin
from .models import RunningLine, RunningText, Contact, ContactsLink, CustomerLink, Requisite


class RunningTextInline(admin.TabularInline):
    model = RunningText


class ContactsLinkInline(admin.TabularInline):
    model = ContactsLink


class CustomerLinkInline(admin.TabularInline):
    model = CustomerLink


@admin.register(RunningLine)
class RunningLineAdmin(admin.ModelAdmin):
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
