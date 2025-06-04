from django.shortcuts import render
from rest_framework import generics

from interview.order.models import Order, OrderTag
from interview.order.serializers import OrderSerializer, OrderTagSerializer, OrderDateRangeFilterSerializer


# Create your views here.
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    

class OrderTagListCreateView(generics.ListCreateAPIView):
    queryset = OrderTag.objects.all()
    serializer_class = OrderTagSerializer


class OrderDateRangeListView(generics.ListAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        filter_serializer = OrderDateRangeFilterSerializer(data=self.request.query_params)
        filter_serializer.is_valid(raise_exception=True)
        start_date = filter_serializer.validated_data['start_date']
        embargo_date = filter_serializer.validated_data['embargo_date']

        return Order.objects.filter(
            start_date__gte=start_date,
            embargo_date__lte=embargo_date,
        )
