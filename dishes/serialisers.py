from django.conf.urls import url, include
from .models import Dish
from rest_framework import routers, serializers, viewsets


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = '__all__'
