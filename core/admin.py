from django.contrib import admin
from .models import *
from .models import Restaurant


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['restaurant', 'subject', 'email', 'timestamp', 'read']
    search_fields = ['restaurant', 'email', 'subject']
    list_filter = ['read']
    date_hierarchy = 'timestamp'


@admin.register(ItemCategory)
class ItemCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'restaurant', 'owner', 'is_active']
    list_filter = ['is_active']
    search_fields = ['name', 'restaurant', 'owner']


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['item_name', 'category', 'restaurant', 'owner', 'is_active']
    list_filter = ['is_active']
    search_fields = ['item_name', 'restaurant']



admin.site.register(Tag)
admin.site.register(ItemReview)
admin.site.register(RestaurantReview)
