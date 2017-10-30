from django.db import models
from parler.models import TranslatableModel


class SeoTag(TranslatableModel):
    meta_description = models.CharField(max_length=200)

    class Meta:
        abstract = True
