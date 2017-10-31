from django.db import models

from seo.models import SeoTag


class Amenitie(models.Model):
    """ Comodidades que presenta una casa/room/hotel"""


class Lodging(SeoTag):
    """ modelo abstracto que se refiere a un hospedaje en general. """
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        abstract = True


class Hotel(Lodging):
    """ hospedaje en hoteles """
    description = models.CharField(max_length=255)


class Home(Lodging):
    """Hospedaje en casas"""
    importance = models.PositiveIntegerField()  # conveniencia/relevancia. se escogen los mas altos para q salgan en la pag princp. en el listado de casas se muestran por defecto ordenados por relevancia.
    max_adults = models.PositiveIntegerField()
