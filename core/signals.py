from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver

from django.contrib.auth.models import User
from .models import Profile, Restaurant


#  Profile Create if not created
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)
        print('Profile created!!!')


#  Profile Update if created
@receiver(post_save, sender=User)
def update_profile(sender, instance, created, **kwargs):
    if created == False:
        instance.profile.save()
        print('Profile updated!!!')


#  Restaurant Create if not created
@receiver(post_save, sender=User)
def create_restaurant(sender, instance, created, **kwargs):
    if created:
        Restaurant.objects.create(owner=instance)
        print('Restaurant created!!!')


#  Restaurant Update if created
@receiver(post_save, sender=User)
def update_restaurant(sender, instance, created, **kwargs):
    if created == False:
        instance.restaurant.save()
        print('Restaurant updated!!!')
