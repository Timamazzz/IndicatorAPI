from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


# Create your models here.
class User(AbstractUser):
    class Meta:
        verbose_name = _("Пользователь")
        verbose_name_plural = _("Пользователи")
