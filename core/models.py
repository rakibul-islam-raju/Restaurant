from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
# from users.models import Restaurant
from django.contrib.auth.models import User


class Profile(models.Model):
    owner = models.OneToOneField(User, to_field='username', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profile_pic = models.ImageField(upload_to='profiles', blank=True, null=True)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=15, unique=True)
    bio = models.TextField(max_length=150, blank=True, null=True)

    def __str__(self):
        return str(self.owner)


class Restaurant(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    slug = models.SlugField(null=True, unique=True)
    phone = models.CharField(max_length=15, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    district = models.CharField(max_length=50)
    police_station = models.CharField(max_length=50)
    address_1 = models.CharField(max_length=50)
    address_2 = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        # return f'{str(self.owner)}\'s restaurant'
        return self.slug

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)



class ItemCategory(models.Model):
    restaurent = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='categories', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Item Categories'

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name    


class Item(models.Model):
    category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    item = models.CharField(max_length=100,)
    image = models.ImageField(upload_to='items')
    price = models.DecimalField(decimal_places=2, max_digits=5)
    discount_price = models.DecimalField(decimal_places=2, max_digits=5, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.item


class Contact(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=254)

    def __str__(self):
        return self.subject


class ItemReview(models.Model):

    Rating_CHOICES = (
        (1, 'Poor'),
        (2, 'Average'),
        (3, 'Good'),
        (4, 'Very Good'),
        (5, 'Excellent')
    )

    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.CharField(max_length=1, default=3)
    text = models.TextField(max_length=250)

    def __str__(self):
        return self.item
    


class RestaurantReview(models.Model):

    Rating_CHOICES = (
        (1, 'Poor'),
        (2, 'Average'),
        (3, 'Good'),
        (4, 'Very Good'),
        (5, 'Excellent')
    )

    restautant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.CharField(max_length=1, default=3)
    text = models.TextField(max_length=250)

    def __str__(self):
        return self.restautant
