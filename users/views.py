from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly
from .serializers import UserProfileSerializer, UserSerializer
from .models import *


class UserProfileView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    lookup_field = 'username'

    def get_queryset(self):
        username = self.kwargs['username']
        uuid = self.kwargs['id']
        return User.objects.filter(username=username, id=uuid)
