from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from lodging.models import Home, Hotel


@admin.register(Home)
class HomeAdmin(TranslationAdmin):
    pass


@admin.register(Hotel)
class HotelAdmin(TranslationAdmin):
    pass
