from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from images.models import Photo
from lodging.models import Home, Hotel, Amenity


@admin.register(Home)
class HomeAdmin(TranslationAdmin):
    list_display = ['name', 'description', 'importance', 'position']
    prepopulated_fields = {'slug': ['name']}
    exclude = ['main_photo', 'photos']

    def save_model(self, request, obj, form, change):
        # super().save_model(request, obj, form, change)
        obj.save()
        folder_to_save = '{0}/{1}'.format('home', obj.id)
        for photo in request.FILES.getlist('photos'):
            obj.photos.add(Photo.objects.create(model=folder_to_save, original=photo))
        obj.main_photo = Photo.objects.create(model=folder_to_save, original=request.FILES['main_photo'])
        obj.save()


@admin.register(Hotel)
class HotelAdmin(TranslationAdmin):
    pass


@admin.register(Amenity)
class AmenityAdmin(TranslationAdmin):
    list_display = ['type', 'amenity', 'font_icon', 'img_icon']
