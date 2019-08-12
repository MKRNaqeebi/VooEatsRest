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
    logo = models.ImageField(upload_to='ShopInterface/media/logo')
    name = models.CharField(
        _('Shop Name'), max_length=128)
    address = models.CharField(
        _('Shop adress'), max_length=256, null=True, blank=True)
    details = models.TextField(null=True, blank=True)
    coordinates = models.CharField(max_length=256)


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


class ProductModel(object):
    """
    2. Model & price (allow them to add more, 
        objective of this is like you sell pizza,
        but we have pure pizza, pizza + topping. 
        Or you selling shirt but you have many size or colors price is differentl. 
        So, we need to add more option in model and set price as individual.
        And for user view must be showed as drop down)
    """
    # price = models.FloatField()
    # name = models.CharField(max_length=256)


class Product(object):
    """
    This is for setting product and add including
    1. Product name
    2. 
    3. Unit price ............... (pieces
    4. Shipping cost ................. (By product, by qty)

    --------------------------------------------------------------------------
    Step 1 : Select shop
    Step 2 : Add product
    Step 3 : Keep personal information for shipping. 
    Step 4 : Selection shipping (Optional related on owner shipping setting. 
        If they allow to have normal delivery and express. 
        This step will be let user to select. 
        If other options, we cannot allow them to select)
    Step 5 : Real-time calculation total amount.

    ------------------------------------------------------
    Please make the user view also. Please make sure that it's responsive by e-mail.
    """

    # name = models.CharField(max_length=256)
    # model = models.ManyToManyField(ProductModel)
    # shipping_cost = models.FloatField()
