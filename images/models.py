from django.db import models

def photo_folder(instance, filename):
    return '{0}/{1}'.format(instance.model, filename)


class Photo(models.Model):
    model = models.CharField(max_length=20)
    original_resized = models.ImageField(upload_to=photo_folder)
    thumbnail = models.ImageField(upload_to=photo_folder)
