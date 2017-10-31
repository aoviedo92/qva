from django.shortcuts import render
from django.views.generic.base import TemplateView

from seo.mixins import SeoMeta


class Index(SeoMeta, TemplateView):
    template_name = 'index.html'
