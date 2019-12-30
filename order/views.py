from django.shortcuts import render
from django.views.generic import ListView, View, TemplateView, FormView
from order.models import Order
from accounts.models import User
from dishes.models import InstanceDish
from order.forms import OrderForm
from django.http import HttpResponseRedirect, HttpResponse

class OrderView(TemplateView):
    model = Order
    template_name = 'order/order.html'
    context_object_name = 'orders'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order = Order.objects.get(user=self.request.user)
        context['dishes'] = order.dishes.all()
        context['full_price'] = order.get_full_price
        return context

    def get_queryset(self):
        return Order.objects.all()

    def del_dish_from_order(self, pk):
        order = Order.objects.first()
        dish = order.dishes.get(id=pk)
        dish.delete()
        order.get_full_price()
        return HttpResponseRedirect("/order")


class MakeOrder(FormView):
    model = Order
    template_name = 'order/orders.html'
    success_url = '/orders/new'
    form_class = OrderForm

    def form_valid(self, form_class):
        Order.objects.create(**form_class.cleaned_data)
        return super().form_valid(form_class)







