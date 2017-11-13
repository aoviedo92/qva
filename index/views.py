from django.views.generic.base import TemplateView
from meta.views import MetadataMixin

from index.mixins import MenuLinkMixin


class Index(MetadataMixin, MenuLinkMixin, TemplateView):
    template_name = 'index.html'
    # use_title_tag = True
    title = 'QVandares | Book Rooms Hotels Tours'
    description = 'qvandares is a platform where you can book hotels, homes, and rooms in Cuba, also, you can book guide Tours'
