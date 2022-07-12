from django.db import models
from django.contrib import admin
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group
from django.utils.safestring import mark_safe
from django_countries.fields import CountryField
from django.urls import reverse_lazy


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('Email is required!'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(email, password, **extra_fields)
        user.is_active = extra_fields.get('is_active', True)
        user.is_staff = True
        user.is_superuser = True

        user.save()
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('Email address'), unique=True, db_index=True)
    username = models.CharField(_('Username'), max_length=40, db_index=True)
    name = models.CharField(
        _('Full name'), max_length=30, blank=True, null=True)

    company_name = models.CharField(
        _('Company name'), max_length=30, null=True, blank=True)

    country = CountryField(
        blank_label='(select country)', blank=True, null=True)
    # Could be e.g. '$' or 'USD'
    currency = models.CharField(
        max_length=3, default='$', help_text=_("Could be e.g. '$' or 'USD'"))

    updated = models.DateTimeField(auto_now=True, db_index=True)
    date_joined = models.DateTimeField(auto_now_add=True, db_index=True)

    # required fields
    is_active = models.BooleanField(
        _('Active'), default=True, help_text=_('Whether the user can login or not.'), db_index=True)
    is_staff = models.BooleanField(_('Staff status'), default=False, help_text=_(
        'Whether the user can login to this dashboard or not.'), db_index=True)
    is_superuser = models.BooleanField(_('Superuser status'), default=False, help_text=_(
        'Grant all permissions regardless of everything, without asigning them one by one.'), db_index=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        ordering = ('-date_joined',)

    @admin.display(description=_('Password'))
    def change_password(self, obj=None):
        return mark_safe("<a href='../password' class='btn btn-primary btn-sm text-white'>%s</a>" % _('Change Password?'))

    @admin.display(description=_('Show invoices'))
    def get_all_invoices_link(self):
        reversed_url = reverse_lazy('admin:invoices_invoice_changelist')
        return mark_safe("<a href='%s?user=%s'>Show invoices</a>" % (reversed_url, self.id))

    @admin.display(description=_('Actions'))
    def show_actions(self):
        return self.get_all_invoices_link()

    def __str__(self):
        return self.email


class CustomGroup(Group):

    class Meta:
        verbose_name = _('group')
