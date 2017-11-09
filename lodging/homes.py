from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from meta.views import Meta

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
    context = {'homes': homes}
    context.update(seted_filters)
    context.update({'meta': Meta(title='Homes & Rooms in Cuba', description='description Homes & Rooms in Cuba',
                                 keywords=['cuba', 'travel', 'rooms'])})
    return render(request, 'homes/home-list.html', context)


class HomeDetail(DetailView):
    model = Home
    context_object_name = 'home'
    template_name = 'homes/home-detail.html'


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
