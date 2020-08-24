from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAuthenticated
from rest_framework.generics import (ListCreateAPIView,
                                    CreateAPIView,
                                    ListAPIView,
                                    RetrieveUpdateDestroyAPIView)
from .models import *
from .serializers import *
from .permissions import *


class HomeView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        items = Item.objects.filter(is_active=True).order_by('-id')
        restaurant = Restaurant.objects.all().order_by('-id')
        item_serialize = ItemSerializer(items, many=True)
        restaurant_serialize = RestaurantSerializer(restaurant, many=True)
        home_serializer = item_serialize.data + restaurant_serialize.data

        return Response(home_serializer)


class RestaurantView(RetrieveUpdateDestroyAPIView):
    serializer_class = RestaurantSerializer
    permission_classes = [IsOwnerOrReadOnly]
    lookup_field = 'slug'

    def get_queryset(self):
        slug = self.kwargs['slug']
        return Restaurant.objects.filter(slug=slug)


class ContactView(CreateAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        slug = self.kwargs['slug']
        try:
            restaurant = Restaurant.objects.get(slug=slug)
            serializer.save(restaurant=restaurant)
        except Restaurant.DoesNotExist:
            raise Http404


class ItemCategoryListView(ListAPIView):
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        try:
            restaurant = Restaurant.objects.get(slug=slug)
            return ItemCategory.objects.filter(restaurant=restaurant, is_active=True).order_by('-id')
        except Restaurant.DoesNotExist:
            raise Http404


class ItemCategoryCreateView(CreateAPIView):
    serializer_class = CategorySerializer
    queryset = ItemCategory.objects.all()
    permission_classes = [IsRestaurantOwner]

    def perform_create(self, serializer):
        try:
            restaurant = Restaurant.objects.get(owner=self.request.user)
            serializer.save(restaurant=restaurant, owner=self.request.user)
        except Restaurant.DoesNotExist:
            raise Http404


class ItemCategoryDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = ItemCategory.objects.filter(is_active=True)
    permission_classes = [IsOwnerOrReadOnly]
    lookup_field = 'id'


class ItemListview(ListAPIView):
    serializer_class = ItemSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        try:
            restaurant = Restaurant.objects.get(slug=slug)
            return Item.objects.filter(restaurant=restaurant, is_active=True)
        except Restaurant.DoesNotExist:
            raise Http404


class ItemCreateView(CreateAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
    permission_classes = [IsRestaurantOwner]

    def perform_create(self, serializer):
        try:
            restaurant = Restaurant.objects.get(owner=self.request.user)
            serializer.save(restaurant=restaurant, owner=self.request.user)
        except Restaurant.DoesNotExist:
            raise Http404


class ItemDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = ItemSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Item.objects.filter(is_active=True)
    lookup_field = 'id'
