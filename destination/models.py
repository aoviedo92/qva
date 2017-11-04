from django.db import models
from django.utils.translation import ugettext_lazy as _


class Province(models.Model):
    prov = models.CharField(max_length=50)


class Destination(models.Model):
    place = models.CharField(max_length=255, help_text=_('Varadero, Vinales, Old Havana'))
    prov = models.ForeignKey(Province)
    description = models.TextField(max_length=200)
