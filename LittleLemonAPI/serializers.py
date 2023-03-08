from .models import MenuItem, Cart, Category
from rest_framework import serializers
from decimal import Decimal
from django.contrib.auth.models import User


class CategorySerializer (serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'slug']

class MenuItemSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all()
    )
    # category = CategorySerializer(read_only=True)
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'category', 'featured']
        extra_kwargs = {'price': {'min_value': 2}}


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'user', 'menuitem', 'quantity', 'unit_price', 'price']
        extra_kwargs = {'price': {'min_value': 0}}