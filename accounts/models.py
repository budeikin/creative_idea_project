from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    MANAGER = "MA"
    FARMER = "FA"
    USER_RULES = (
        (FARMER, "Farmer"),
        (MANAGER, "Manager")
    )

    username = None
    email = models.EmailField(_("email address"), unique=True)
    role = models.CharField(
        max_length=2,
        choices=USER_RULES
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
