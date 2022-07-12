from django.contrib import admin

from .models import Invoice


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('invoice_number', 'amount', 'is_paid', 'date')
    fields = ('amount', 'user', 'is_paid')
    list_filter = ('is_paid', 'date')
    autocomplete_fields = ('user',)

    def has_delete_permission(self, req, obj=None):
        return False
