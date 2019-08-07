from datetime import datetime
from enum import unique

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class User(AbstractUser):
    ''' 
    Customize django User functionality 
    '''
    contact_number = models.CharField(
        _('Contact Number'), max_length=32, null=True, blank=True)
