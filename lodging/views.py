from django.shortcuts import render
from django.views.generic.base import TemplateView

from seo.mixins import SeoMeta


class A(SeoMeta, TemplateView):
    title = "mi custom title"
    meta_description = "jo jo jo"
    template_name = 'base.html'
