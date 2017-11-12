from django import template
from django.conf import settings
from djmoney_rates.utils import convert_money

register = template.Library()


@register.filter
def set_currency(value, request):
    currency_session = request.session.get(settings.CURRENCY_SESSION_KEY, settings.DEFAULT_CURRENCY)
    money = convert_money(value, settings.DEFAULT_CURRENCY, currency_session)
    # se puede usar %.2f para mostrar en la plantilla los centavos. 75.50
    return '%d %s' % (money.amount, money.currency)


@register.simple_tag
def get_available_currencies():
    return settings.CURRENCIES


@register.simple_tag(takes_context=True)
def get_current_currency(context):
    return context['request'].session.get(settings.CURRENCY_SESSION_KEY, settings.DEFAULT_CURRENCY)


@register.inclusion_tag('includes/price.html')
def set_currency(request, price):
    """
    usado para poder estilizar el precio y el currency. un template tag si puede devolver html, miestras q
    es custom filter solo puede devolver str
    """
    currency_session = request.session.get(settings.CURRENCY_SESSION_KEY, settings.DEFAULT_CURRENCY)
    money = convert_money(price, settings.DEFAULT_CURRENCY, currency_session)
    return {'amount': '%d' % money.amount, 'currency': money.currency}
