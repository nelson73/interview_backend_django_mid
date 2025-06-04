
from django.urls import path
from interview.order.views import OrderListCreateView, OrderTagListCreateView, OrderDateRangeListView

urlpatterns = [
    path('tags/', OrderTagListCreateView.as_view(), name='order-detail'),
    path('filter-by-date/', OrderDateRangeListView.as_view(), name='order-filter-by-date'),
    path('', OrderListCreateView.as_view(), name='order-list'),
]