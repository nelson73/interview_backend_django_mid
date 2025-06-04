
from django.urls import path
from interview.order.views import OrderListCreateView, OrderTagListCreateView, OrderDeactivateView, \
    OrderRetrieveUpdateDestroyView

urlpatterns = [
    path('tags/', OrderTagListCreateView.as_view(), name='order-detail'),
    path('deactivate/<int:id>/', OrderDeactivateView.as_view(), name='order-deactivate'),
    path('orders/<int:id>/', OrderRetrieveUpdateDestroyView.as_view(), name='order-detail'),
    path('', OrderListCreateView.as_view(), name='order-list'),
]