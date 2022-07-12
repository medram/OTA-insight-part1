import random


def generate_invoice_number():
    # to avoid circular imports
    from .models import Invoice

    number = random.randint(0, 99999)
    if Invoice.objects.filter(invoice_number=number).exists():
        return generate_invoice_number()
    return f'OTA-{number:05d}'
