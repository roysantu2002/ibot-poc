from accounts.models import User
from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.db import models
from django.forms import CharField, Textarea, TextInput
from django.utils.translation import gettext_lazy as _
from djongo import models
from rest_framework_simplejwt import token_blacklist


class UserAdminConfig(UserAdmin):
    model = User

    search_fields = ('email', 'user_name', 'first_name',)
    list_filter = ('email', 'user_name', 'first_name', 'is_active', 'is_staff')
    ordering = ['id']
    list_display = ('email', 'user_name', 'first_name',
                    'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'first_name',)}),
        (
            _('Permissions'), {'fields': ('is_staff', 'is_active', 'is_superuser')}

        ),
        (_('Important dates'), {'fields': ('last_login',)}),
        ('Personal', {'fields': ('about',)}),
    )
    readonly_fields = ['last_login']
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 60})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'first_name', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser')}
         ),
    )

# class OutstandingTokenAdmin(token_blacklist.admin.OutstandingTokenAdmin):
#
#     def has_delete_permission(self, *args, **kwargs):
#         return True # or whatever logic you want
#
# admin.site.unregister(token_blacklist.models.OutstandingToken)
# admin.site.register(token_blacklist.models.OutstandingToken, OutstandingTokenAdmin)

admin.site.register(User, UserAdminConfig)