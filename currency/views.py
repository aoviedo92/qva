from django import http
from django.conf import settings
from django.utils.http import is_safe_url, urlunquote

CURRENCY_QUERY_PARAMETER = 'currency'
CURRENCY_SESSION_KEY = CURRENCY_QUERY_PARAMETER


def set_currency(request):
    """
    Redirect to a given url while setting the chosen language in the
    session or cookie. The url and the language code need to be
    specified in the request parameters.

    Since this view changes how the user will see the rest of the site, it must
    only be accessed as a POST request. If called as a GET request, it will
    redirect to the page in the request (the 'next' parameter) without changing
    any state.
    """
    next = request.POST.get('next', request.GET.get('next'))
    if ((next or not request.is_ajax()) and
            not is_safe_url(url=next, allowed_hosts={request.get_host()}, require_https=request.is_secure())):
        next = request.META.get('HTTP_REFERER')
        if next:
            next = urlunquote(next)  # HTTP_REFERER may be encoded.
        if not is_safe_url(url=next, allowed_hosts={request.get_host()}, require_https=request.is_secure()):
            next = '/'
    response = http.HttpResponseRedirect(next) if next else http.HttpResponse(status=204)
    if request.method == 'POST':
        currency_code = request.POST.get(CURRENCY_QUERY_PARAMETER)
        if currency_code and currency_code in ['USD', 'EUR']:
            if next:
                response = http.HttpResponseRedirect(next)
            if hasattr(request, 'session'):
                request.session[CURRENCY_SESSION_KEY] = currency_code
            else:
                response.set_cookie(
                    'currency', currency_code,
                    max_age=settings.LANGUAGE_COOKIE_AGE,
                    path=settings.LANGUAGE_COOKIE_PATH,
                    domain=settings.LANGUAGE_COOKIE_DOMAIN,
                )
    return response
