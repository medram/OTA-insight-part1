from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import Group
from .models import CustomUser, CustomGroup


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'is_active',
                    'is_staff', 'date_joined', 'show_actions')
    list_display_links = ('email',)
    readonly_fields = ('show_actions',)
    list_filter = ('is_active', 'is_staff', 'is_superuser',
                   'updated', 'date_joined', 'last_login')
    search_fields = ('email', 'username', 'name')
    readonly_fields = ('change_password', 'updated',
                       'date_joined', 'last_login')
    filter_horizontal = ('user_permissions', 'groups')

    ordering = ('-date_joined',)

    fieldsets = (
        (None, {
            'fields': ('username', 'email', 'name', 'company_name', 'country', 'currency', 'change_password')
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
