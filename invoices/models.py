from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from .utils import generate_invoice_number

# User class
User = get_user_model()


class Invoice(models.Model):
    invoice_number = models.CharField(
        max_length=9, default=generate_invoice_number, unique=True, db_index=True)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateTimeField(
        _('Created at'), auto_now_add=True, db_index=True)
    is_paid = models.BooleanField(default=False, blank=True)
    user = models.ForeignKey(
        User, related_name='invoices', on_delete=models.CASCADE)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.invoice_number

    def __repr__(self):
        return f'<Invoice {self.invoice_number}>'
