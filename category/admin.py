from django.contrib import admin

# Register your models here.

from django.contrib import admin

from category.models import Category, CategoryCountry

# Register your models here.

admin.site.register(Category)
admin.site.register(CategoryCountry)
