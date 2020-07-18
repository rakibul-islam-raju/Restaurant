# from django.db import models
# from django.urls import reverse
# from django.template.defaultfilters import slugify
# from django.contrib.auth.models import User


# class Profile(models.Model):
#     owner = models.OneToOneField(User, to_field='username', on_delete=models.CASCADE)
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     profile_pic = models.ImageField(upload_to='profiles', blank=True, null=True)
#     email = models.EmailField(max_length=100, unique=True)
#     phone = models.CharField(max_length=15, unique=True)
#     bio = models.TextField(max_length=150, blank=True, null=True)

#     def __str__(self):
#         return str(self.owner)


# class Restaurant(models.Model):
#     owner = models.OneToOneField(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=50)
#     slug = models.SlugField(null=True, unique=True)
#     phone = models.CharField(max_length=15, unique=True)
#     email = models.EmailField(max_length=100, unique=True)
#     district = models.CharField(max_length=50)
#     police_station = models.CharField(max_length=50)
#     address_1 = models.CharField(max_length=50)
#     address_2 = models.CharField(max_length=50, blank=True, null=True)

#     def __str__(self):
#         # return f'{str(self.owner)}\'s restaurant'
#         return self.slug

#     def get_absolute_url(self):
#         return reverse('article_detail', kwargs={'slug': self.slug})

#     def save(self, *args, **kwargs):
#         if not self.slug:
#             self.slug = slugify(self.name)
#         return super().save(*args, **kwargs)
