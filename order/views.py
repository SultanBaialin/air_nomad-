from rest_framework.generics import CreateAPIView, ListCreateAPIView
from order.serializers import OrderSerializer
from rest_framework.response import Response


class CreatedOrderView(ListCreateAPIView):
    serializer_class = OrderSerializer

    def get(self, request, *args, **kwargs):
        user = request.user
        orders = user.orders.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=200)
