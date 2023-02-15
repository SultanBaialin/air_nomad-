from django.contrib.auth import get_user_model
from django.db import models
from category.models import Category, CountryCategory
from ckeditor.fields import RichTextField

User = get_user_model()


class Product(models.Model):
    STATUS_CHOISES =(
        ('in_stock', 'активен'),
        ('out_of_stock', 'неактивен')
    )

    owner = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='products')
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    country_category = models.ForeignKey(CountryCategory, related_name='country', on_delete=models.RESTRICT)

    city = models.CharField(max_length=60)
    address = models.CharField(max_length=60)
    house_number = models.PositiveSmallIntegerField()
    flat_number = models.PositiveSmallIntegerField(blank=True)

    guests = models.PositiveSmallIntegerField()
    rooms = models.PositiveSmallIntegerField()
    beds = models.PositiveSmallIntegerField()
    bathrooms = models.PositiveSmallIntegerField()

    wifi = models.BooleanField(default=False)
    fridge = models.BooleanField(default=False)
    air_conditioner = models.BooleanField(default=False)
    tv = models.BooleanField(default=False)
    pool = models.BooleanField(default=False)
    furniture = models.BooleanField(default=False)
    washing = models.BooleanField(default=False)
    medicine = models.BooleanField(default=False)
    kitchen = models.BooleanField(default=False)

    image1 = models.ImageField(upload_to='images')
    image2 = models.ImageField(upload_to='images')
    image3 = models.ImageField(upload_to='images')

    title = models.CharField(max_length=150)
    description = RichTextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    stock = models.CharField(choices=STATUS_CHOISES, max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ProductImages(models.Model):
    title = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='images/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')

