from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.db import models
from utils.choices import Operation_systems, Browsers

class User(AbstractUser):

    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None
    last_name = None
    is_tasix = models.BooleanField(default=False)
    operatsion_system = models.TextField(max_length=31, choices=Operation_systems.choices, default=Operation_systems.WINDOWS)
    browser = models.TextField(max_length=31, choices=Browsers.choices, default=Browsers.CHROME)



