from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from images.models import Photo
from lodging.models import Home, Hotel, Amenity


@admin.register(Home)
class HomeAdmin(TranslationAdmin):
    list_display = ['name', 'description', 'importance', 'destination']
    prepopulated_fields = {'slug': ['name']}
    exclude = ['main_photo', 'photos']
    filter_horizontal = ('amenities',)
    list_filter = ('amenities', 'importance', 'destination')
    search_fields = ('name', 'description')

    def position_map(self, instance):
        if instance.position is not None:
            return '<img src="http://maps.googleapis.com/maps/api/staticmap?center=%(latitude)s,%(longitude)s&zoom=%(zoom)s&size=%(width)sx%(height)s&maptype=roadmap&markers=%(latitude)s,%(longitude)s&sensor=false&visual_refresh=true&scale=%(scale)s" width="%(width)s" height="%(height)s">' % {
                'latitude': instance.position.latitude,
                'longitude': instance.position.longitude,
                'zoom': 15,
                'width': 100,
                'height': 100,
                'scale': 2
            }

    position_map.allow_tags = True

    def save_model(self, request, obj, form, change):
        # super().save_model(request, obj, form, change)
        photos = request.FILES.getlist('photos')
        main_photo = request.FILES.get('main_photo', None)
        folder_to_save = '{0}/{1}'.format('home', obj.id)
        if main_photo:
            obj.main_photo = Photo.objects.create(model=folder_to_save, original=main_photo)
        obj.save()
        if photos:
            for photo in photos:
                obj.photos.add(Photo.objects.create(model=folder_to_save, original=photo))

                # obj.save()


@admin.register(Hotel)
class HotelAdmin(TranslationAdmin):
    pass


@admin.register(Amenity)
class AmenityAdmin(TranslationAdmin):
    list_display = ['type', 'amenity', 'font_icon', 'img_icon']
