from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from users.models import User


class Restaurant(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    slug = models.SlugField(null=True, blank=True) # TODO: make Unique
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    district = models.CharField(max_length=50)
    police_station = models.CharField(max_length=50)
    address_1 = models.CharField(max_length=50)
    address_2 = models.CharField(max_length=50, blank=True, null=True)
    birthday_party = models.BooleanField(blank=True, null=True)
    marrige_party = models.BooleanField(blank=True, null=True)
    smoking_zone = models.BooleanField(blank=True, null=True)
    business = models.BooleanField(blank=True, null=True)
    conference = models.BooleanField(blank=True, null=True)
    kids_zone = models.BooleanField(blank=True, null=True)
    couple_space = models.BooleanField(blank=True, null=True)
    Capacity = models.BooleanField(blank=True, null=True)
    ac = models.BooleanField(blank=True, null=True)
    washroom = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return str(self.owner)

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
    item_name = models.CharField(max_length=100)
    quantity_or_size = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='items')
    price = models.DecimalField(decimal_places=2, max_digits=5)
    discount_price = models.DecimalField(decimal_places=2, max_digits=5, blank=True, null=True)
    is_parcel = models.BooleanField()
    Perparing_time = models.DecimalField(decimal_places=0, max_digits=3, help_text='Minuites Only', blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.item_name


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
    rating = models.CharField(max_length=1)
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
    rating = models.CharField(max_length=1)
    text = models.TextField(max_length=250)

    def __str__(self):
        return self.restautant
