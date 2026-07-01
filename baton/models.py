from __future__ import annotations

from typing import Any

from django.db import models
from django.utils.translation import gettext_lazy as _

class BatonTheme(models.Model):
    id = models.AutoField(primary_key=True, verbose_name=_("id"))
    name = models.CharField(_("name"), max_length=255)
    theme = models.TextField(_("theme"))
    active = models.BooleanField(_("active"), default=False)

    def __str__(self) -> str:
        return self.name

    # override save, only one theme can be active
    def save(self, *args: Any, **kwargs: Any) -> None:
        if self.active:
            self.__class__.objects.exclude(pk=self.pk).update(active=False)
        super(BatonTheme, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("admin theme")
        verbose_name_plural = _("admin themes")
