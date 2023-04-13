from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from orders.models import Product, Order
from orders.serializers import ProductModelSerializer, OrderModelSerializer


class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.order_by('-created_at')
    serializer_class = ProductModelSerializer


class OrderModelViewSet(ModelViewSet):
    queryset = Order.objects.order_by('-created_at')
    serializer_class = OrderModelSerializer

