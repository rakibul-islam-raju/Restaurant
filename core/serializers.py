from rest_framework import serializers
from users.models import User
from .models import *


class RestaurantSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Restaurant
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    model = User
    fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ItemCategory
        exclude = ['restaurant', 'owner', 'is_active']


class ItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Item
        fields = ['category',
                'item_name',
                'quantity_or_size',
                'image',
                'price',
                'discount_price',
                'is_parcel',
                'Perparing_time',
                'description']


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        exclude = ['restaurant']


class ItemReviewSerilizer(serializers.ModelSerializer):

    class Meta:
        model = ItemReview
        fields = '__all__'


class RestaurantReviewSerilizer(serializers.ModelSerializer):

    class Meta:
        model = RestaurantReview
        fields = '__all__'

