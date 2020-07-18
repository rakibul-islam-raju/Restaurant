from rest_framework.generics import RetrieveUpdateDestroyAPIView

from .permissions import IsOwnerOrReadOnly
from .serializers import *
from .models import *


class ProfileView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    lookup_field = 'owner'

    def get_queryset(self):
        owner = self.kwargs['owner']
        return Profile.objects.filter(owner=owner)


class RestaurantView(RetrieveUpdateDestroyAPIView):
    serializer_class = RestaurantSerializer
    permission_classes = [IsOwnerOrReadOnly]
    lookup_field = 'slug'
    queryset = Restaurant.objects.all()

    def get_queryset(self):
        slug = self.kwargs['slug']
        return Restaurant.objects.filter(slug=slug)
