from django.conf import settings


def debug(request):
    print(settings.DEBUG)
    return {'DEBUG': settings.DEBUG}
