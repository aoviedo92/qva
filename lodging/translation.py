from modeltranslation.translator import register

from lodging.models import Lodging, Home, Hotel
from seo.translation import SeoTranslationOptions


@register(Lodging)
class LodgingTranslationOptions(SeoTranslationOptions):
    fields = ('name',)


@register(Home)
class HomeTranslationOptions(LodgingTranslationOptions):
    fields = ()


@register(Hotel)
class HotelTranslationOptions(LodgingTranslationOptions):
    fields = ('description',)
