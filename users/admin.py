from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email',
                    'username',
                    'is_seller',
                    'is_buyer',
                    'last_login',
                    'is_staff',
                    'date_joined')
    search_fields = ('email',
                    'username')
    readonly_fields = ('date_joined',
                        'last_login')

    filter_horizontal = ()
    list_filter = ('is_seller', 'is_buyer')
    fieldsets = ()

