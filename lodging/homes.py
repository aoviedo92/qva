from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from meta.views import Meta, MetadataMixin

from index.mixins import MenuLinkMixin
from lodging.models import Home
from seo.mixins import ModelMetaView

# FBV deprecated helper
# def apply_filters(get_params):
#     filters = {}
#     cant_adults = get_params.get('cant_adults', '')
#     min_price = get_params.get('min_price', '')
#     max_price = get_params.get('max_price', '')
#     # destination = get_request.get('destination', '')
#     if cant_adults:
#         filters.update({'max_guest': cant_adults})
#     if min_price:
#         filters.update({'price__gte': min_price})
#     if max_price:
#         filters.update({'price__lte': max_price})
#     chosen_filters = {'cant_adults': cant_adults, 'min_price': min_price, 'max_price': max_price}
#     qs = Home.objects.filter(**filters)
#     return qs, chosen_filters

# FCV deprecated
# def home_list(request):
#     homes, chosen_filters = apply_filters(request.GET)
#     paginator = Paginator(homes, 6)
#     page = request.GET.get('page', 1)
#     try:
#         homes = paginator.page(page)
#     except EmptyPage:
#         homes = paginator.page(paginator.num_pages)
#     except PageNotAnInteger:
#         homes = paginator.page(1)
#     context = {'homes': homes, MenuLinkMixin.use_context_var: 'homes'}
#     context.update(chosen_filters)
#
#     context.update({'meta': Meta(use_title_tag=True, title='Homes & Rooms in Cuba',
#                                  description='description Homes & Rooms in Cuba',
#                                  keywords=['cuba', 'travel', 'rooms'])})
#     return render(request, 'homes/home-list.html', context)


class HomeDetail(ModelMetaView, DetailView):
    model = Home
    context_object_name = 'home'
    template_name = 'homes/home-detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # TODO: mejorar esto (se pone .filter dos veces, debe haber una mejor manera)
        context['basic_amenities'] = self.object.amenities.filter(type='basic')
        context['secondary_amenities'] = self.object.amenities.filter(type='secondary')
        return context


class HomeList(MetadataMixin, MenuLinkMixin, ListView):
    # TODO: add GOOD description, keywords
    # TODO: i18n
    menu_link_active = 'homes'
    title = 'Homes & Rooms in Cuba'
    description = 'description Homes & Rooms in Cuba'
    keywords = ['cuba', 'travel', 'rooms']
    model = Home
    template_name = 'homes/home-list.html'
    context_object_name = 'homes'
    paginate_by = 6
    chosen_filters = {}

    def get_queryset(self):
        # TODO: terminar los filtros destination y room_type
        get_params = self.request.GET
        filters = {}
        cant_adults = get_params.get('cant_adults', '')
        min_price = get_params.get('min_price', '')
        max_price = get_params.get('max_price', '')
        if cant_adults:
            filters.update({'max_guest': cant_adults})
        if min_price:
            filters.update({'price__gte': min_price})
        if max_price:
            filters.update({'price__lte': max_price})
        self.chosen_filters = {'cant_adults': cant_adults, 'min_price': min_price, 'max_price': max_price}
        return Home.objects.filter(**filters)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.chosen_filters)
        return context
