from .models import Order
from django.shortcuts import render
from order.models import Order
from django.views.generic import ListView, View, TemplateView, FormView


def show_order(request):
    return {'order': Order.objects.get(user=request.user)}