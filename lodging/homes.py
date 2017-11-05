from django.views.generic.list import ListView

from lodging.models import Home


class HomeList(ListView):
    model = Home
    template_name = 'homes/home-list.html'
