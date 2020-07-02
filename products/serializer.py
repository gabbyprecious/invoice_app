from rest_framework import serializers

from .models import Product, Order

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'price', 'description', 'image')

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'product', 'quantity', 'date', 'user')
