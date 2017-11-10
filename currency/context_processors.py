def get_currency(request):
    return {'CURRENCY_CODE': request.session.get("currency", 'USD')}
