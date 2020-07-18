from django.contrib import admin
from .models import *
from .models import Profile, Restaurant

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email']
    prepopulated_fields = {'slug': ('name',)} 



admin.site.register(Profile)
admin.site.register(Contact)
admin.site.register(Tag)
admin.site.register(ItemCategory)
admin.site.register(Item)
admin.site.register(ItemReview)
admin.site.register(RestaurantReview)
