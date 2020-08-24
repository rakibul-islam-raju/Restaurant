from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import User
from core.models import Restaurant


#  Restaurant Create if not created
@receiver(post_save, sender=User)
def create_restaurant(sender, instance, created, **kwargs):
    if instance.is_seller:
        print('User is seller')
        if created:
            Restaurant.objects.create(
                owner = instance,
                name = instance.restaurant_name,
                email = instance.email,
                phone = instance.phone
                )
            print('Restaurant created!!!')
