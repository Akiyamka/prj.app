"""Certificate type model for certification app"""

from django.db import models
from django.utils.translation import ugettext_lazy as _


class CertificateType(models.Model):
    name = models.CharField(
        help_text=_('Certificate type.'),
        max_length=200,
        null=False,
        blank=False
    )

    description = models.TextField(
        help_text=_('Certificate type description - 1000 characters limit.'),
        max_length=1000,
        null=True,
        blank=True,
    )

    printed_text = models.CharField(
        help_text=_(
            'Wording that will be placed on certificate. '
            'e.g. "Has attended and completed".'
        ),
        max_length=500,
        null=False,
        blank=False
    )

    order = models.IntegerField(
        blank=True,
        null=True,
        unique=True
    )

    def __str__(self):
        return self.name
