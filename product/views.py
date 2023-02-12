from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, response
from rest_framework.decorators import action

from .models import Product
from . import serializers
from .permission import IsAuthor


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.ProductListSerializer
        return serializers.ProductSerializer

    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy'):
            return [permissions.IsAuthenticated(), IsAuthor()]
        return [permissions.IsAuthenticatedOrReadOnly()]


# from django.shortcuts import render
# from favorite.models import Favorite
# @action(['POST', 'DELETE'], detail=True)
#     def favorite(self, request, pk):
#         product = self.get_object()
#         user = request.user
#         if request.method == 'POST':
#             if user.favorites.filter(product=product).exists():
#                 return Response('This product is already in favorites!',
#                                 status=400)
#             Favorites.objects.create(owner=user, product=product)
#             return Response('Added to favorites!', status=201)
#         else:
#             if user.favorites.filter(product=product).exists():
#                 user.favorites.filter(product=product).delete()
#                 return Response('Deleted from favorites!', status=204)
#             return Response('Product is not found!', status=400)
