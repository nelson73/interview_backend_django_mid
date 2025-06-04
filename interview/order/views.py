from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from interview.order.models import Order, OrderTag
from interview.order.serializers import OrderSerializer, OrderTagSerializer


# Create your views here.
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderTagListCreateView(generics.ListCreateAPIView):
    queryset = OrderTag.objects.all()
    serializer_class = OrderTagSerializer


class OrderDeactivateView(APIView):
    def post(self, request, order_id, *args, **kwargs):
        try:
            order = Order.objects.get(id=order_id)
            order.is_active = False
            order.save()
        except Order.DoesNotExist:
            return Response({'detail': 'Order not found.'}, status=status.HTTP_404_NOT_FOUND)

        return Response({'detail': f'Order {order_id} has been deactivated.'}, status=status.HTTP_200_OK)


class OrderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Alternative more generic drf view that handles most stuff

    PATCH /123/
    Content-Type: application/json

    {
      "is_active": false
    }
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'id'
