from django.shortcuts import render
from django.views.generic import ListView, View, TemplateView, FormView
from order.models import Order, ShippingOrder
from accounts.models import User
from dishes.models import InstanceDish
from order.forms import OrderForm, ShippingOrderForm, EditCountDish
from django.http import HttpResponseRedirect, HttpResponse


class OrderView(TemplateView):
    model = Order
    template_name = "order/order.html"
    context_object_name = 'orders'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not self.request.user.is_authenticated:
            order = Order.objects.first()
        else:
            order, created = \
                Order.objects.get_or_create(user=self.request.user)
        return context

    def get_queryset(self):
        return Order.objects.all()

    def del_dish_from_order(self, pk):
        order = Order.objects.first()
        dish = order.dishes.get(id=pk)
        dish.delete()
        order.get_full_price()
        return HttpResponseRedirect("/order")


class EditCountDish(FormView):
    template_name = 'order/order.html'
    form_class = EditCountDish
    success_url = "/order"

    def get_queryset(self, *args, **kwargs):
        return Order.objects.all()

    def form_valid(self, form_class):
        data = form_class.cleaned_data
        new_count = data['new_count']
        print(new_count)
        dish_id = data['dish_id']
        print(dish_id)
        order = Order.objects.first()
        dish = order.dishes.get(id=dish_id)
        print(dish.count)
        dish.count = new_count
        dish.save()
        order.get_full_price()
        # return HttpResponseRedirect("/order")
        return super().form_valid(form_class)

    def form_invalid(self, form_class):
        print("Some problems")
        return super().form_invalid(form_class)

        # for price in Dish.objects.values_list('price', flat=True):
        #     new_price = price + change_price
        #     Dish.objects.filter(price=price).update(price=new_price)
        # return super().form_valid(form_class)


# class MakeOrder(FormView):
#     model = Order
#     template_name = 'order/orders.html'
#     success_url = '/order/'
#     form_class = OrderForm
#
#     def form_valid(self, form_class):
#         Order.objects.create(**form_class.cleaned_data)
#         return super().form_valid(form_class)
#
#     def edit_count_dish(self, pk, new_count):
#         order = Order.objects.first()
#         dish = order.dishes.get(id=pk)
#         print(new_count)
#         dish.count = new_count
#         order.get_full_price()
#         return HttpResponseRedirect("/order")


class MakeShippingOrderForm(FormView):
    model = ShippingOrder
    template_name = 'order/shipping_form.html'
    success_url = '/'
    form_class = ShippingOrderForm

    def form_valid(self, form_class):
        ShippingOrder.objects.create(**form_class.cleaned_data)
        return super().form_valid(form_class)
