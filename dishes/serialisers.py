from django.conf.urls import url, include
from .models import Dish, InstanceDish
from accounts.models import User
from order.models import Order
from rest_framework import routers, serializers, viewsets, status, generics


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = '__all__'


class OrderUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email']


class OrderDishesSerializer(serializers.ModelSerializer):
    price = serializers.IntegerField()

    class Meta:
        model = InstanceDish
        fields = ['name', 'price']


class OrderSerializer(serializers.ModelSerializer):
    dishes = OrderDishesSerializer(many=True)
    user = OrderUserSerializer()
    full_price = serializers.IntegerField()

    class Meta:
        model = Order
        fields = '__all__'
