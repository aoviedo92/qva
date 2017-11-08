from io import BytesIO
from uuid import uuid4

from PIL import Image as Img
from django.db import models

QUALITY_THUMB = 90
QUALITY_RESIZE_1200x800 = 95


def photo_folder(instance, filename):
    return '{0}/{1}'.format(instance.model, filename)


class Photo(models.Model):
    DEFAULT_WIDTH = 1200
    DEFAULT_HEIGHT = 800
    model = models.CharField(max_length=20)
    original = models.ImageField(upload_to=photo_folder)
    thumbnail = models.ImageField(upload_to=photo_folder)

    def make_thumbnail(self, image, photo_saved_name):
        thumb_saved_name = 'thumb-' + photo_saved_name
        thumb = Img.open(image)
        thumb.thumbnail((300, 300), Img.ANTIALIAS)
        b_thumb = BytesIO()
        thumb.save(b_thumb, 'JPEG', quality=QUALITY_THUMB)
        # llamar con save=false para no crear un ciclo de llamadas, ya q al hacer save llama al
        # self.save q a su vez vuelve a llamar a make_thumbnail. aqui se llama a self.thumbnail.save
        # y no se hace simplemente como self.original pq este fichero nunca se subio. ademas el self.original
        # es conveniente setearlo por separado, primero la imagen 'resizada o no' y luego el nombre
        self.thumbnail.save(name=thumb_saved_name, content=b_thumb, save=False)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.original:
            image = Img.open(self.original)
            w, h = image.size
            photo_saved_name = '%s.jpg' % uuid4()
            if w > 1200 and h > 800:
                # resizar y hacer thumbnail con la imagen resizada obtenida
                image = image.resize((Photo.DEFAULT_WIDTH, Photo.DEFAULT_HEIGHT), Img.ANTIALIAS)
                image_resized = BytesIO()
                image.save(image_resized, 'JPEG', quality=QUALITY_RESIZE_1200x800)
                self.original.file = image_resized
                self.make_thumbnail(image_resized, photo_saved_name)
            else:
                # si no hay q resizar solo hacer thumbnail con la img original
                self.make_thumbnail(self.original, photo_saved_name)
            self.original.name = photo_saved_name

        super().save(force_insert, force_update, using, update_fields)
