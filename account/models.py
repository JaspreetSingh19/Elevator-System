"""
This file contains 'User' model for registering the user
"""
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from account.managers.user_manager import UserRequestManager
from elevator.models import TimeStampedModel


class User(AbstractBaseUser, PermissionsMixin, TimeStampedModel):
    """
    Custom user model that extends the built-in Django User model
    with additional fields for User model
    * email is unique
    """
    first_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    contact = models.CharField(max_length=20, unique=True, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    objects = UserRequestManager()

    def __str__(self):
        string = f"{self.first_name} {self.last_name}"
        return string

    class Meta:
        """
        Use the Meta class to specify the database table
        for User model
        """
        db_table = 'User'
