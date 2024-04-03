from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import RunningLine, Requisite, Contact, PrivacyPolicy
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def ensure_single_active(sender_model):
    @receiver(pre_save, sender=sender_model)
    def _ensure_single_active(sender, instance, **kwargs):
        if instance.is_active:
            active_count = sender_model.objects.filter(is_active=True).exclude(pk=instance.pk).count()
            if active_count > 0:
                raise ValidationError(_('Может быть только один активный объект!'))


ensure_single_active(RunningLine)
ensure_single_active(Requisite)
ensure_single_active(Contact)
ensure_single_active(PrivacyPolicy)
