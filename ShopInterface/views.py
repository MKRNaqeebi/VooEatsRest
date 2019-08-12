from rest_framework import generics, permissions
from .models import Shop
from .serializers import ShopSerializer

# Create your views here.

class ShopViewSet(generics.ListCreateAPIView):
    """ API endpoint that sorts the circuits by given parameter """
    permission_classes = (permissions.AllowAny,)
    serializer_class = ShopSerializer
    queryset = Shop.objects.all()
    
    def perform_create(self, serializer):
        instance = serializer.save(owner = self.request.user)
