from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _
from django.views.generic.list import ListView

from lodging.models import Home


def apply_filters(get_params):
    filters = {}
    cant_adults = get_params.get('cant_adults', '')
    min_price = get_params.get('min_price', '')
    max_price = get_params.get('max_price', '')
    # destination = get_request.get('destination', '')
    if cant_adults:
        filters.update({'max_guest': cant_adults})
    if min_price:
        filters.update({'price__gte': min_price})
    if max_price:
        filters.update({'price__lte': max_price})
    seted_filters = {'cant_adults': cant_adults, 'min_price': min_price, 'max_price': max_price}
    qs = Home.objects.filter(**filters)
    return qs, seted_filters


def home_list(request):
    homes, seted_filters = apply_filters(request.GET)
    paginator = Paginator(homes, 6)
    page = request.GET.get('page', 1)
    try:
        homes = paginator.page(page)
    except EmptyPage:
        homes = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        homes = paginator.page(1)
    context = {'homes': homes, 'title': _('Homes & Rooms in Cuba')}
    context.update(seted_filters)
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
