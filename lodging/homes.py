from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.utils.translation import ugettext_lazy as _

from lodging.models import Home


def home_list(request):
    homes = Home.objects.all()
    paginator = Paginator(homes, 8)
    page = request.GET.get('page')
    try:
        homes = paginator.page(page)
    except PageNotAnInteger:
        homes = paginator.page(1)
    except EmptyPage:
        if request.is_ajax():
            return HttpResponse('')
        homes = paginator.page(paginator.num_pages)
    context = {'homes': homes, 'title': _('Homes & Rooms in Cuba')}
    if request.is_ajax():
        return render(request, 'homes/includes/list.html', context)
    return render(request, 'homes/home-list.html', context)


class HomeList(ListView):
    model = Home
    template_name = 'homes/home-list.html'
