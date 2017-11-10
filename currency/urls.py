from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^setlang/$', views.set_currency, name='set_currency'),
]
