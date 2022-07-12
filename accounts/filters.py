from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()


class UsersBilledOverAmountFilter(admin.SimpleListFilter):
    title = _('User billed amount')

    parameter_name = 'over_amount'

    def lookups(self, request, model_admin):
        return (
            (1000, _('Over 1,000')),
            (5000, _('Over 5,000')),
            (10000, _('Over 10,000')),
        )

    def queryset(self, request, queryset):
        if self.value() is not None:
            filter_value = int(self.value())

            if filter_value == 1000:
                return queryset.filter(invoices__amount__gte=1000).distinct()

            if filter_value == 5000:
                return queryset.filter(invoices__amount__gte=5000).distinct()

            if filter_value == 10000:
                return queryset.filter(invoices__amount__gte=10000).distinct()
