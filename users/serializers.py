from rest_framework import serializers
from .models import *


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'phone',
            'picture',
        ]


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['first_name',
                'last_name',
                'username',
                'email',
                'phone',
                'picture',
                'is_buyer',
                'is_seller',
                'restaurant_name',
                'password',
                'password2']
        extra_kwargs = {
            'password': {
                'write_only':True
            }
        }

    def validate(self, data):
        if not data['is_buyer'] and not data['is_seller']:
            raise serializers.ValidationError("Buyer or Seller is required required.")
        if data['is_buyer'] and data['is_seller']:
            raise serializers.ValidationError("Please select one between Buyer and Seller.")
        if not data['is_seller'] and data['restaurant_name']:
            raise serializers.ValidationError("Please select you as a seller for set your restaurant name.")
        if data['is_seller'] and not data['restaurant_name']:
            raise serializers.ValidationError("Please select your restaurant name.")
        return data
    
    def save(self, request):
        user = User(
            first_name = self.validated_data['first_name'],
            last_name = self.validated_data['last_name'],
            username = self.validated_data['username'],
            email = self.validated_data['email'],
            phone = self.validated_data['phone'],
            picture = self.validated_data['picture'],
            is_buyer = self.validated_data['is_buyer'],
            is_seller = self.validated_data['is_seller'],
            restaurant_name = self.validated_data['restaurant_name'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password':'Passwords must match.'})
        user.set_password(password)
        user.save()
        return user
