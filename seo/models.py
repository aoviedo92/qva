from django.db import models


class SeoTag(models.Model):
    title = models.CharField(max_length=200, blank=True)
    meta_description = models.TextField(max_length=200, blank=True)

    class Meta:
        abstract = True
