from rest_framework import permissions
from .models import Restaurant
from users.models import User


class IsOwnerOrReadOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


class IsRestaurantOwner(permissions.BasePermission):
    message = 'You don\'t have any restaurant'

    def has_permission(self, request, view):
        return request.user.is_seller

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class IsBuyer(permissions.BasePermission):
    message = 'You are not able to review'

    def has_permission(self, request, view):
        return request.user.is_buyer
