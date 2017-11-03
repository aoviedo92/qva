from io import BytesIO
from uuid import uuid4

from PIL import Image as Img
from django.db import models


def photo_folder(instance, filename):
    return '{0}/{1}'.format(instance.model, filename)


class Photo(models.Model):
    DEFAULT_WIDTH = 1200
    DEFAULT_HEIGHT = 800
    model = models.CharField(max_length=20)
    original = models.ImageField(upload_to=photo_folder)
    thumbnail = models.ImageField(upload_to=photo_folder)

    def make_thumbnail(self, image):
        thumb = Img.open(image)
        thumb.thumbnail((200, 200), Img.ANTIALIAS)
        b_thumb = BytesIO()
        thumb.save(b_thumb, 'JPEG', quality=75)
        self.thumbnail.save(name='%s-thumb.jpg' % uuid4(), content=b_thumb, save=False)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.original:
            image = Img.open(self.original)
            w, h = image.size
            if w > 1200 and h > 800:
                image = image.resize((Photo.DEFAULT_WIDTH, Photo.DEFAULT_HEIGHT), Img.ANTIALIAS)
                image_resized = BytesIO()
                image.save(image_resized, 'JPEG', quality=90)
                self.original.file = image_resized
                self.make_thumbnail(image_resized)
            else:
                self.make_thumbnail(self.original)
            self.original.name = '%s.jpg' % uuid4()

        super().save(force_insert, force_update, using, update_fields)
