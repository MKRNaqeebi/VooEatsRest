from django.db import models
from django.utils.translation import gettext_lazy as _
from AuthInterface.models import User

# Create your models here.


class Shop(models.Model):
    ''' 
    They can add/ edit /delete details of shop including
    1. Add logo picture (We will limit to square with 2MB size)
    2. Add shop name 
    3. Add shop address and details (Optional)
    '''
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    contact_number = models.CharField(
        _('Contact Number'), max_length=32, null=True, blank=True)
    logo = models.ImageField()
    name = models.CharField(
        _('Shop Name'), max_length=128)
    address = models.CharField(
        _('Shop adress'), max_length=256, null=True, blank=True)
    details = models.TextField(null=True, blank=True)


class ShopMember(models.Model):
    ''' 
    They also can add member to manage their account
    Admin = can do everything as owner
    Editor = can do everything except billing
    Sender = can do only order management 

    We will limit the a number of member and shop details add based on subscription plan
    Please see more in subscription plan

    '''
    ROLE_CHOICES = (
        ('sender', 'Sender'),
        ('editor', 'Editor'),
        ('admin', 'Admin'),
    )
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(
        max_length=16, choices=ROLE_CHOICES, default='sender')
