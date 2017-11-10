from django import template

register = template.Library()


@register.filter
def set_currency(value, request):
    currency_session = request.session.get("currency", 'USD')
    return '%d %s' % (value, currency_session)
