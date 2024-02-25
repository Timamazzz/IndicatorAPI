from django.db import models


class RunningLine(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название бегущей строки')
    is_active = models.BooleanField(default=False, verbose_name='Активно')

    class Meta:
        verbose_name = 'Бегущая строка'
        verbose_name_plural = 'Бегущие строки'

    def __str__(self):
        return self.name


class RunningText(models.Model):
    line = models.ForeignKey(RunningLine, on_delete=models.CASCADE, related_name='running_texts',
                             verbose_name='Бегущая строка')
    text = models.TextField(verbose_name='Текст бегущей строки')

    class Meta:
        verbose_name = 'Текст бегущей строки'
        verbose_name_plural = 'Тексты бегущих строк'


class Contact(models.Model):
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    email = models.EmailField(verbose_name='Email')
    is_active = models.BooleanField(default=False, verbose_name='Активно')

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class ContactsLink(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    url = models.URLField(verbose_name='URL')
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='urls', verbose_name='Контакт')

    class Meta:
        verbose_name = 'Ссылка контакта'
        verbose_name_plural = 'Ссылки контакта'


class CustomerLink(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название ссылки')
    url = models.URLField(verbose_name='URL ссылки')

    class Meta:
        verbose_name = 'Ссылка заказчика'
        verbose_name_plural = 'Ссылки заказчиков'


class Requisite(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование')
    certificate = models.CharField(max_length=100, verbose_name='Свидетельство')
    inn = models.CharField(max_length=12, verbose_name='ИНН')
    ogrnip = models.CharField(max_length=15, verbose_name='ОГРНИП')
    checking_account = models.CharField(max_length=20, verbose_name='Расчетный счет')
    bik = models.CharField(max_length=9, verbose_name='БИК')
    bank = models.CharField(max_length=255, verbose_name='Банк')
    correspondent_account = models.CharField(max_length=20, verbose_name='Корреспондентский счет')
    is_active = models.BooleanField(default=False, verbose_name='Активно')

    class Meta:
        verbose_name = 'Реквизит'
        verbose_name_plural = 'Реквизиты'
