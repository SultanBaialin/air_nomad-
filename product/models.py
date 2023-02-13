from django.contrib.auth import get_user_model
from django.db import models
from category.models import Category, CategoryCountry
from ckeditor.fields import RichTextField

User = get_user_model()


class Product(models.Model):
    STATUS_CHOISES =(
        ('in_stock', 'активен'),
        ('out_of_stock', 'неактивен')
    )

    owner = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='products')
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    country_category = models.ForeignKey(CategoryCountry, related_name='country', on_delete=models.RESTRICT)

    city = models.CharField(max_length=60)
    address = models.CharField(max_length=60)
    house_number = models.SmallIntegerField()
    flat_number = models.SmallIntegerField()

    guests = models.SmallIntegerField()
    rooms = models.SmallIntegerField()
    beds = models.SmallIntegerField()
    bathrooms = models.SmallIntegerField()

    wifi = models.BooleanField()
    fridge = models.BooleanField()
    air_conditioner = models.BooleanField()
    tv = models.BooleanField()
    pool = models.BooleanField()
    furniture = models.BooleanField()
    washing = models.BooleanField()
    medicine = models.BooleanField()
    kitchen = models.BooleanField()

    title = models.CharField(max_length=150)
    description = RichTextField()
    image1 = models.ImageField(upload_to='images')
    image2 = models.ImageField(upload_to='images')
    image3 = models.ImageField(upload_to='images')
    image4 = models.ImageField(upload_to='images')
    image5 = models.ImageField(upload_to='images')
    price = models.DecimalField(max_digits=12, decimal_places=2)
    stock = models.CharField(choices=STATUS_CHOISES, max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

