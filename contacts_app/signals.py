from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import RunningLine, Requisite, Contact
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


@receiver(pre_save, sender=RunningLine)
def ensure_single_active_running_line(sender, instance, **kwargs):
    if instance.is_active:
        active_lines_count = RunningLine.objects.filter(is_active=True).exclude(pk=instance.pk).count()
        if active_lines_count > 0:
            raise ValidationError(_('Может быть только одна активная строка!'))


@receiver(pre_save, sender=Requisite)
def ensure_single_active_requisite(sender, instance, **kwargs):
    if instance.is_active:
        requisites_count = Requisite.objects.filter(is_active=True).exclude(pk=instance.pk).count()
        if requisites_count > 0:
            raise ValidationError(_('Может быть только один активный реквизит!'))


@receiver(pre_save, sender=Contact)
def ensure_single_active_contact(sender, instance, **kwargs):
    if instance.is_active:
        contacts_count = Contact.objects.filter(is_active=True).exclude(pk=instance.pk).count()
        if contacts_count > 0:
            raise ValidationError(_('Может быть только один активный контакт!'))
