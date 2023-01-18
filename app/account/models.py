"""
ibots auth user model
"""
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):

    """
    ibots user manager
    """
    def create_superuser(self, email, password=None, **other_fields):

        """ create a new ibots super user"""
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        user = self.create_user(email, password, **other_fields)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **other_fields):

        """ create a new ibots user"""

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, **other_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):

    """
    ibots user system
    """

    id = models.BigAutoField(
                auto_created = True,
                unique=True,
                primary_key = True,
                serialize = False,
                verbose_name ='id')
    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(max_length=150,  blank=True)
    first_name = models.CharField(max_length=150, blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    about = models.TextField(_(
        'about'), max_length=500, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['user_name', 'first_name']

    def __str__(self):
        return self.email


    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email


    # this methods are require to login super user from admin panel
    def has_perm(self, perm, obj=None):
        return self.is_staff

    # this methods are require to login super user from admin panel
    def has_module_perms(self, app_label):
        return self.is_staff