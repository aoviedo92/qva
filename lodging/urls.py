from django.conf.urls import url, include
from . import homes
urlpatterns = [
    url(r'^$', homes.HomeList.as_view()),
]