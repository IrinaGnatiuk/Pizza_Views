from django.views.generic.base import View
from django.shortcuts import redirect, render_to_response, reverse, render
from django.http import JsonResponse
from .models import Dish, InstanceDish
from order.models import Order


class DishesApiView(View):

    def get(self, request):
        sort = request.GET.get('sort')
        id = request.GET.get('id')
        name = request.GET.get('name')
        price = request.GET.get('price')
        price_more = request.GET.get('price_more')
        price_less = request.GET.get('price_less')
        dishes = Dish.objects.all()
        if sort:
            dishes = Dish.objects.all().order_by(sort)
        if id:
            dishes = Dish.objects.all().filter(id=id)
        if name:
            dishes = Dish.objects.all().filter(name=name)
        if price:
            dishes = Dish.objects.all().filter(price=price)
        if price_more:
            dishes = Dish.objects.all().filter(price__gt=price_more)
        if price_less:
            dishes = Dish.objects.all().filter(price__lt=price_less)
        serialize_dishes = []
        for dish in dishes:
            serialize_dishes.append(dish.get_serialize_dishes())
        return JsonResponse({'dishes_list': serialize_dishes})


class OrderApiView(View):

    def get(self, request):
        if not request.user.is_authenticated:
            order = Order.objects.first()
        else:
            order = Order.objects.get(user=request.user)
        serialize_order = order.get_serialize_order()
        return JsonResponse({'order': serialize_order})


class DishesAddOrderApiView(View):

    def get(self, request):
        return JsonResponse(
            {'message': "method GET not supported. Please use POST"}
        )

    def post(self, request, *args, **kwargs):
        dish = Dish.objects.get(id=request.POST.get('id'))
        name = dish.name
        count = int(request.POST.get('count'))
        id = request.POST.get('id')
        instance_dish = InstanceDish.objects.filter(dish_template=id)
        if instance_dish:
            instance_dish = InstanceDish.objects.get(dish_template=id)
            instance_dish.count += count
            instance_dish.save()
        else:
            instance_dish = dish.create_instance_dish(count)
        if not self.request.user.is_authenticated:
            order = Order.objects.first()
            order.dishes.add(instance_dish)
        else:
            order, created = \
                Order.objects.get_or_create(user=self.request.user)
            order.dishes.add(instance_dish)
        order.get_full_price()
        serialize_order = order.get_serialize_order()
        return JsonResponse(
            {'order update': serialize_order,
             'добавлено блюдо': name,
             "в количестве": count}
        )
