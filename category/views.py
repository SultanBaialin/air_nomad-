from django.shortcuts import render

# Create your views here.


from django.shortcuts import render
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from category import serializers
from category.models import Category, CountryCategory
import logging

# Create your views here.
logger = logging.getLogger('main')


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer

    def get_permissions(self):
        if self.action in ('retrieve', 'list'):
            logger.info('listing, retrieve')
            return [permissions.AllowAny()]
        else:
            logger.warning('Only admin')
            return [permissions.IsAdminUser()]


class CountryCategoryViewSet(ModelViewSet):
    queryset = CountryCategory.objects.all()
    serializer_class = serializers.CategorySerializer

    def get_permissions(self):
        if self.action in ('retrieve', 'list'):
            logger.info('allow')
            return [permissions.AllowAny()]
        else:
            logger.warning('only admin')
            return [permissions.IsAdminUser()]