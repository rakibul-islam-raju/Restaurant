from rest_framework import serializers
from .models import *


class RestaurantSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Restaurant
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'



class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ItemCategory
        fields = '__all__'
        # exclude = ['is_active']


class ItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Item
        exclude = ['is_active']


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = '__all__'

    # def create(self, validated_data):
    #     return Contact(**validated_data)

    def save(self):
        email = self.validated_data['email']
        message = self.validated_data['message']
        send_email(from=email, message=message)


class ItemReviewSerilizer(serializers.ModelSerializer):

    class Meta:
        model = ItemReview
        fields = '__all__'


class RestaurantReviewSerilizer(serializers.ModelSerializer):

    class Meta:
        model = RestaurantReview
        fields = '__all__'

