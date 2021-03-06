from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import Group
from .models import CustomUser, CustomGroup
from .filters import UsersBilledOverAmountFilter


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'is_active',
                    'is_staff', 'show_total_amount', 'date_joined', 'show_actions')
    list_display_links = ('email',)
    readonly_fields = ('show_actions', 'show_total_amount')
    list_filter = (UsersBilledOverAmountFilter, 'is_active', 'is_staff', 'is_superuser',
                   'updated', 'date_joined', 'last_login')
    search_fields = ('email', 'username', 'name')
    readonly_fields = ('change_password', 'recent_invoices', 'total_invoiced_amount_past_12_months', 'updated',
                       'date_joined', 'last_login')
    filter_horizontal = ('user_permissions', 'groups')

    ordering = ('-date_joined',)

    fieldsets = (
        (None, {
            'fields': ('username', 'email', 'name', 'company_name', 'country', 'currency', 'change_password')
        }),
        (_('Recent invoices info'), {
            'fields': ('total_invoiced_amount_past_12_months', 'recent_invoices')
        }),
        (_('Permissions & Groups'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        (_('More info'), {
            'fields': ('updated', 'date_joined', 'last_login')
        }),
    )

    add_fieldsets = (
        (None, {
            'fields': ('username', 'email', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser')
        }),
    )


admin.site.unregister(Group)


@admin.register(CustomGroup)
class GroupAdmin(GroupAdmin):
    pass
