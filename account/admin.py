"""
This file contain admin to register models in admin panel
"""
from django.contrib import admin

from account.models import User


class UserAdmin(admin.ModelAdmin):
    """
    Custom admin 'UserAdmin' for model 'User' to register
    model in the admin panel
    """
    list_display = ('id', 'first_name', 'last_name', 'email', 'contact', 'password')

    class Meta:
        """
        Use the Meta class to specify the model
        for 'UserAdmin'
        """
        model = User


admin.site.register(User, UserAdmin)
