from modeltranslation.translator import TranslationOptions, translator, register

from seo.models import SeoTag


@register(SeoTag)
class SeoTranslationOptions(TranslationOptions):
    fields = ('meta_description', 'title',)

