from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Shop(models.Model):
    ''' 
    Shop  
    '''
    contact_number = models.CharField(
        _('Contact Number'), max_length=32, null=True, blank=True)
