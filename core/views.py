from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.generics import (ListCreateAPIView,
                                    CreateAPIView,
                                    ListAPIView,
                                    RetrieveUpdateDestroyAPIView)

from .models import *
from .serializers import *
from .permissions import *


class UserProfileView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsOwnerOrReadOnly]
    lookup_field = 'user'

    def get_queryset(self):
        owner = self.kwargs['owner']
        return Profile.objects.filter(owner=owner)


# class ProfileView(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, APIView):

#     def get(self, request, format=None):

#     def retrieve(request, *args, **kwargs):
    
#     def update(request, *args, **kwargs):
    
#     def destroy(request, *args, **kwargs):



class RestaurantView(RetrieveUpdateDestroyAPIView):
    serializer_class = RestaurantSerializer
    permission_classes = [IsOwnerOrReadOnly]
    lookup_field = 'slug'
    queryset = Restaurant.objects.all()

    def get_queryset(self):
        slug = self.kwargs['slug']
        return Restaurant.objects.filter(slug=slug)


class HomeView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        items = Item.objects.filter(is_active=True).order_by('-id')
        restaurant = Restaurant.objects.all().order_by('-id')
        item_serialize = ItemSerializer(items, many=True)
        restaurant_serialize = RestaurantSerializer(restaurant, many=True)
        home_serializer = item_serialize.data + restaurant_serialize.data

        return Response(home_serializer)


# class ContactView(CreateAPIView):
#     serializer_class = ContactSerializer
#     queryset = Contact.objects.all().order_by('-id')
#     permission_classes = [AllowAny]


class ItemCategoryView(ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = ItemCategory.objects.filter(is_active=True).order_by('-id')
    permission_classes = [IsAuthenticatedOrReadOnly] # TODO: change permission to isOwnerOrReadOnly


# class ItemCategoryDetailView(RetrieveUpdateDestroyAPIView):
