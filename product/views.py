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
