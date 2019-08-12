from rest_framework import serializers
from .models import Shop

class ShopSerializer(serializers.ModelSerializer):

    class Meta:

        model = Shop
        fields = ('id', 'contact_number', 'logo', 'name', 'address', 'details', 'coordinates', )
