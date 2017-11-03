from django.db import models
from django.utils.translation import ugettext_lazy as _

from images.models import Photo
from seo.models import SeoTag


class Amenitie(models.Model):
    """ Comodidades que presenta una casa/room/hotel"""


class Lodging(SeoTag):
    """ modelo abstracto que se refiere a un hospedaje en general. """
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        abstract = True
        verbose_name = _('Lodging')
        verbose_name_plural = _('Lodgings')


class Hotel(Lodging):
    """ hospedaje en hoteles """
    description = models.CharField(max_length=255)

    class Meta:
        verbose_name = _('Hotel')
        verbose_name_plural = _('Hotels')


class Home(Lodging):
    """Hospedaje en casas"""
    importance = models.PositiveIntegerField()  # conveniencia/relevancia. se escogen los mas altos para q salgan en la pag princp. en el listado de casas se muestran por defecto ordenados por relevancia.
    max_guest = models.PositiveIntegerField()
    bedrooms = models.PositiveIntegerField()
    beds = models.PositiveIntegerField()
    baths = models.PositiveIntegerField()
    weekly_discount = models.PositiveIntegerField(blank=True, null=True)
    monthly_discount = models.PositiveIntegerField(blank=True, null=True)
    cleaning_fee = models.PositiveIntegerField(blank=True, null=True)
    house_rules = models.TextField()
    main_photo = models.OneToOneField(Photo, blank=True, null=True, related_name='home_main_photo')
    photos = models.ManyToManyField(Photo, related_name='home_photos')

    class Meta:
        verbose_name = _('Home')
        verbose_name_plural = _('Homes')

    def __str__(self):
        return self.name