from django.conf.urls import url, include
from . import homes
urlpatterns = [
    url(r'^homes/', homes.HomeList.as_view(), name='home_list'),
]