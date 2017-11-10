from django import template
from moneyed import Money
from djmoney_rates.utils import convert_money
register = template.Library()


@register.filter
def set_currency(value, request):
    currency_session = request.session.get("currency", 'USD')
    # return '%d %s' % (value, currency_session)
    return convert_money(value, "USD", currency_session)
