from django.conf.urls import url, include
from . import homes
urlpatterns = [
    # url(r'^homes/', homes.home_list, name='home_list'),
    url(r'^homes/', homes.HomeList.as_view(), name='home_list'),
    url(r'^homes/(?P<slug>[-\w]+)/$', homes.HomeList.as_view(), name='home_detail'),
]