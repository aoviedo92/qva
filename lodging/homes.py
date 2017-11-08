from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _
from django.views.generic.list import ListView

from lodging.models import Home


def apply_filters(get_request, qs):
    cant_adults = get_request.get('cant-adults', '')
    if cant_adults:
        qs = qs.filter(max_guest=int(cant_adults))
    seted_filters = {'cant_adults': cant_adults}
    return qs, seted_filters


def home_list(request):
    homes, seted_filters = apply_filters(request.GET, Home.objects.all())
    # homes = Home.objects.all()
    # homes = range(1000)
    paginator = Paginator(homes, 6)
    page = request.GET.get('page', 1)
    try:
        print('try page %s' % page)
        homes = paginator.page(page)
    except EmptyPage:
        print('empty page')
        homes = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        print('page not an int')
        homes = paginator.page(1)
    context = {'homes': homes, 'title': _('Homes & Rooms in Cuba')}
    context.update(seted_filters)
    # if request.is_ajax():
    #     return render(request, 'homes/includes/list.html', context)
    return render(request, 'homes/home-list.html', context)


class HomeList(ListView):
    model = Home
    template_name = 'homes/home-list.html'
    context_object_name = 'homes'
    paginate_by = 6

    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     get = self.request.GET
    #     cant_adults = int(get.get('cant-adults', 0))
    #     if cant_adults:
    #         qs = qs.filter(max_guest=cant_adults)
    #     return qs
