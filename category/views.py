from django.shortcuts import render

# Create your views here.


from django.shortcuts import render
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from category import serializers
from category.models import Category, CountryCategory


# Create your views here.

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer

    def get_permissions(self):
        if self.action in ('retrieve', 'list'):
            return [permissions.AllowAny()]
        else:
            return [permissions.IsAdminUser()]


class CountryCategoryViewSet(ModelViewSet):
    queryset = CountryCategory.objects.all()
    serializer_class = serializers.CategorySerializer

    def get_permissions(self):
        if self.action in ('retrieve', 'list'):
            return [permissions.AllowAny()]
        else:
            return [permissions.IsAdminUser()]