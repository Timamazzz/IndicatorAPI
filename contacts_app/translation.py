# translation.py
from modeltranslation.translator import TranslationOptions, translator
from .models import RunningLine, RunningText, ContactsLink, CustomerLink, Requisite


class RunningLineTranslationOptions(TranslationOptions):
    fields = ('name',)


class RunningTextTranslationOptions(TranslationOptions):
    fields = ('text',)


class ContactsLinkTranslationOptions(TranslationOptions):
    fields = ('name',)


class CustomerLinkTranslationOptions(TranslationOptions):
    fields = ('name',)


class RequisiteTranslationOptions(TranslationOptions):
    fields = ('name', 'bank')


translator.register(RunningLine, RunningLineTranslationOptions)
translator.register(RunningText, RunningTextTranslationOptions)
translator.register(ContactsLink, ContactsLinkTranslationOptions)
translator.register(CustomerLink, CustomerLinkTranslationOptions)
translator.register(Requisite, RequisiteTranslationOptions)
