from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import truncatechars
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from geoposition.fields import GeopositionField
from meta.models import ModelMeta
from model_utils import Choices
from model_utils.models import TimeStampedModel

from destination.models import Destination
from images.models import Photo
from seo.models import SeoTag


class Amenity(models.Model):
    """ Comodidades que presenta una casa/room/hotel"""
    TYPE_CHOICES = Choices(('basic', _('Basic')), ('secondary', _('Secondary')))
    type = models.CharField(choices=TYPE_CHOICES, default=TYPE_CHOICES.basic, max_length=20)
    amenity = models.CharField(max_length=100)
    font_icon = models.CharField(max_length=20, blank=True)
    img_icon = models.CharField(max_length=20, blank=True)

    class Meta:
        verbose_name_plural = _('Amenities')
        verbose_name = _('Amenity')

    def __str__(self):
        return self.amenity

        # @staticmethod
        # def secondaries():
        #     return Amenity.objects.filter(type=Amenity.TYPE_CHOICES.secondaries)
        #
        # @staticmethod
        # def basics():
        #     return Amenity.objects.filter(type=Amenity.TYPE_CHOICES.basic)


class Lodging(ModelMeta, TimeStampedModel):
    """ modelo abstracto que se refiere a un hospedaje en general. """
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField()
    amenities = models.ManyToManyField(Amenity)
    destination = models.ForeignKey(Destination, null=True, blank=True)
    position = GeopositionField(null=True, blank=True,
                                default='23.1135925,-82.36659559999998')  # 23.1135925,-82.36659559999998
    price = models.PositiveIntegerField()
    _metadata = {
        'title': 'name',
        'description': 'meta_description',
    }

    def meta_description(self):
        return truncatechars(self.description, 150)

    class Meta:
        abstract = True


class Hotel(Lodging):
    """ hospedaje en hoteles """

    class Meta:
        verbose_name = _('Hotel')
        verbose_name_plural = _('Hotels')


class Home(Lodging):
    """Hospedaje en casas"""
    # conveniencia/relevancia. se escogen los mas altos para q salgan en la pag princp. en el listado de casas
    #  se muestran por defecto ordenados por relevancia.
    ROOM_TYPE = Choices(('entire_room', _('Entire home')), ('shared_room', _('Shared room')),
                        ('private_room', _('Shared room')))
    importance = models.PositiveIntegerField()
    max_guest = models.PositiveIntegerField()
    bedrooms = models.PositiveIntegerField()
    beds = models.PositiveIntegerField()
    baths = models.PositiveIntegerField()
    weekly_discount = models.PositiveIntegerField(blank=True, null=True)
    monthly_discount = models.PositiveIntegerField(blank=True, null=True)
    cleaning_fee = models.PositiveIntegerField(blank=True, null=True)
    house_rules = models.TextField()
    main_photo = models.ForeignKey(Photo, blank=True, null=True)
    photos = models.ManyToManyField(Photo, related_name='home_photos')
    host = models.OneToOneField(User, null=True, blank=True)
    type = models.CharField(choices=ROOM_TYPE, default=ROOM_TYPE.entire_room, max_length=20)

    class Meta:
        verbose_name = _('Home')
        verbose_name_plural = _('Homes')
        ordering = ['-importance']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('lodging:home_detail', kwargs={'slug': self.slug})

    def similares(self):
        return Home.objects.exclude(id=self.id).filter(
            type=self.type,
            destination=self.destination,
            beds__gte=self.beds - 1, beds__lte=self.beds + 1,  # una cama mas, una cama menos
        )
