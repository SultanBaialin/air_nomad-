from django.contrib import admin

# Register your models here.

from django.contrib import admin

from category.models import Category, Category_Country

# Register your models here.

admin.site.register(Category)
admin.site.register(Category_Country)
