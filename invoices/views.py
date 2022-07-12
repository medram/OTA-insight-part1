from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from .models import Invoice

User = get_user_model()

# No need to use Django-rest-framwork for just one endpoint.


def invoices(req, user_id):
    status_code = 200
    result = {
        'success': True,
        'data': None,
        'errors': None
    }

    try:
        user = User.objects.get(id=int(user_id))
        invoices = Invoice.objects.filter(user=user, is_paid=False).all()
        parsed_invoices = [{
            'invoice_number': invoice.invoice_number,
            'amount': invoice.amount,
            'currency': user.currency,
            'date': invoice.date
        } for invoice in invoices]

        result['data'] = parsed_invoices

    except User.DoesNotExist:
        status_code = 404
        result['success'] = False
        result['errors'] = _('User does not exist!')

    return JsonResponse(result, status=status_code)
