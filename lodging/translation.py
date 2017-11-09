from modeltranslation.translator import register, TranslationOptions

from lodging.models import Lodging, Home, Hotel, Amenity
from seo.translation import SeoTranslationOptions


@register(Lodging)
class LodgingTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Home)
class HomeTranslationOptions(LodgingTranslationOptions):
    fields = ()


@register(Hotel)
class HotelTranslationOptions(LodgingTranslationOptions):
    fields = ('description',)


@register(Amenity)
class AmenityTranslationOption(TranslationOptions):
    fields = ('amenity',)
