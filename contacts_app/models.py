from django.db import models
from django.utils.translation import gettext_lazy as _


class RunningLine(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Название бегущей строки'))
    is_active = models.BooleanField(default=False, verbose_name=_('Активно'))

    class Meta:
        verbose_name = _('Бегущая строка')
        verbose_name_plural = _('Бегущие строки')

    def __str__(self):
        return self.name


class RunningText(models.Model):
    line = models.ForeignKey(RunningLine, on_delete=models.CASCADE, related_name='running_texts',
                             verbose_name=_('Бегущая строка'))
    text = models.TextField(verbose_name=_('Текст бегущей строки'))

    class Meta:
        verbose_name = _('Текст бегущей строки')
        verbose_name_plural = _('Тексты бегущих строк')


class Contact(models.Model):
    phone = models.CharField(max_length=20, verbose_name=_('Телефон'))
    email = models.EmailField(verbose_name=_('Email'))
    is_active = models.BooleanField(default=False, verbose_name=_('Активно'))

    class Meta:
        verbose_name = _('Контакт')
        verbose_name_plural = _('Контакты')


class ContactsLink(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Название'))
    url = models.URLField(verbose_name=_('URL'))
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='urls', verbose_name=_('Контакт'))

    class Meta:
        verbose_name = _('Ссылка контакта')
        verbose_name_plural = _('Ссылки контакта')


class CustomerLink(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Название ссылки'))
    url = models.URLField(verbose_name=_('URL ссылки'))

    class Meta:
        verbose_name = _('Ссылка заказчика')
        verbose_name_plural = _('Ссылки заказчиков')


class Requisite(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Наименование'))
    certificate = models.CharField(max_length=100, verbose_name=_('Свидетельство'))
    inn = models.CharField(max_length=12, verbose_name=_('ИНН'))
    ogrnip = models.CharField(max_length=15, verbose_name=_('ОГРНИП'))
    checking_account = models.CharField(max_length=20, verbose_name=_('Расчетный счет'))
    bik = models.CharField(max_length=9, verbose_name=_('БИК'))
    bank = models.CharField(max_length=255, verbose_name=_('Банк'))
    correspondent_account = models.CharField(max_length=20, verbose_name=_('Корреспондентский счет'))
    is_active = models.BooleanField(default=False, verbose_name=_('Активно'))

    class Meta:
        verbose_name = _('Реквизит')
        verbose_name_plural = _('Реквизиты')


class PrivacyPolicy(models.Model):
    text = models.TextField(verbose_name=_('Текст правил использования и политики конфиденциальности'))
    is_active = models.BooleanField(default=False, verbose_name=_('Активно'))

    class Meta:
        verbose_name = _('Правила использования и политика конфиденциальности')
        verbose_name_plural = _('Правила использования и политика конфиденциальности')
