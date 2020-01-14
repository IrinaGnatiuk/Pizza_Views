from .models import Order
from django.shortcuts import render
from order.models import Order
from django.views.generic import ListView, View, TemplateView, FormView
from accounts.models import User


def show_order(request):
    if not request.user.is_authenticated:
        return {'orders': Order.objects.first()}
    return {'orders': Order.objects.get(user=request.user)}