from rest_framework.serializers import ModelSerializer

from orders.models import Product, Order, Category


class ProductModelSerializer(ModelSerializer):
    class Meta:
        model = Product
        exclude = ()


class OrderModelSerializer(ModelSerializer):
    class Meta:
        model = Order
        exclude = ()


class CategorySerialzier(ModelSerializer):
    class Meta:
        model = Category
        exlude = ()
