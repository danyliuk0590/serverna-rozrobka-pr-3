from rest_framework import serializers
from .models import Product, ProductCategory, Basket, BasketItem


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['id', 'name']


class ProductSerializer(serializers.ModelSerializer):
    categories = ProductCategorySerializer(many=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'categories']


class BasketItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = BasketItem
        fields = ['id', 'product', 'quantity']


class BasketSerializer(serializers.ModelSerializer):
    items = BasketItemSerializer(many=True)

    class Meta:
        model = Basket
        fields = ['id', 'created_at', 'updated_at', 'status', 'items']
