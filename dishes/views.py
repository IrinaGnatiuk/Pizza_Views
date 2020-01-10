from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from django.views.generic import ListView, View, TemplateView, DetailView
from django.views.generic.edit import FormView, UpdateView
from dishes.models import *
from order.models import Order
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
from .serialisers import *


class InstanceDishView(ListView):
    model = InstanceDish
    context_object_name = 'instance_dish'
    template_name = 'dishes/dishes.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_instance_dish'] = \
            InstanceDish.objects.values().order_by('name')
        return context

    def get_quertyset(self, *args, **kwargs):
        return InstanceDish.objects.all()


class DrinkView(ListView):
    model = Drink
    template_name = 'dishes/drinks_list.html'
    queryset = Drink.objects.order_by("price")
    context_object_name = 'drink'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_var'] = 'DrinkListView'
        return context

    def get_quertyset(self, *args, **kwargs):
        return Drink.objects.all()


class DishViewList(ListView):
    model = Dish
    template_name = 'dishes/dishes_list.html'
    context_object_name = 'dishes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_var'] = 'DishesListView'
        context['count_dish'] = Dish.objects.count()
        context['list_dish1'] = Dish.objects.values('price').order_by('price')
        context['list_dish2'] = Dish.objects.values_list('name', flat=True).order_by('price')
        context['filter200'] = Dish.objects.filter(price__gt = 200)
        context['filter50'] = Dish.objects.filter(price__gt=50)
        return context


class IngredientViewList(ListView):
    model = Ingredient
    template_name = 'dishes/ingredient_list.html'
    queryset = Ingredient.objects.order_by("name")
    context_object_name = 'ingredients'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_var'] = 'IngredientListView'
        return context

    def get_queryset(self, *args, **kwargs):
        return Ingredient.objects.all()


class IngredientView(View):
    model = Ingredient
    context_object_name = 'ingredient'
    template_name = 'dishes/ingredient.html'

    def get(self, request, *args, **kwargs):
        return HttpResponse("INGREDIENT(View)!!!")


class DishDetailView(DetailView):
    model = Dish
    template_name = 'dishes/dish.html'


class DrinkDetailView(DetailView):
    model = Drink
    template_name = 'dishes/drink.html'


class StartView(TemplateView):
    model = Ingredient
    context_object_name = 'ingredient'
    template_name = 'dishes/start.html'


class MakeIngredient(FormView):
    model = Ingredient
    template_name = 'dishes/ingredients.html'
    success_url = '/'
    form_class = IngredientForm

    def form_valid(self, form_class):
        Ingredient.objects.create(**form_class.cleaned_data)
        return super().form_valid(form_class)

    def form_invalid(self, form_class):
        print("Some problems")
        return super().form_invalid(form_class)


class MakeDrink(FormView):
    model = Drink
    template_name = 'dishes/drinks_form.html'
    success_url = "/"
    form_class = DrinkForm

    def form_valid(self, form_class):
        Drink.objects.create(**form_class.cleaned_data)
        return super().form_valid(form_class)


class MakeDishes(FormView):
    model = Dish
    template_name = 'dishes/dishes_form.html'
    success_url = '/dishes/list'
    form_class = DishForm

    def form_valid(self, form_class):
        Dish.objects.create(**form_class.cleaned_data)
        return super().form_valid(form_class)


class UpdateDrink(UpdateView):
    form_class = DrinkForm
    model = Drink
    template_name = 'dishes/drinks_form.html'
    success_url = '/'


class UpdateIngredient(UpdateView):
    form_class = IngredientForm
    model = Ingredient
    template_name = 'dishes/ingredients.html'
    success_url = '/'


class UpdateDish(UpdateView):
    form_class = DishForm
    model = Dish
    template_name = 'dishes/dishes_form.html'
    success_url = '/dishes/list'


class CreateNewPrice(FormView):
    template_name = 'dishes/new_price.html'
    form_class = ChangePriceForm
    model = ChangePrice
    success_url = '/dishes/list'

    def get_queryset(self, *args, **kwargs):
        return Dish.objects.all()

    def form_valid(self, form_class):
        data = form_class.cleaned_data
        change_price = data['change_price']
        for price in Dish.objects.values_list('price', flat=True):
            new_price = price + change_price
            Dish.objects.filter(price=price).update(price=new_price)
        return super().form_valid(form_class)


class MakeSort(FormView):
    template_name = 'dishes/sort.html'
    form_class = SortForm
    model = SortDish
    success_url = '/dishes/list'
    Dish.objects.all().order_by('price')

    def form_valid(self, form_class):
        data = form_class.cleaned_data
        sort = data['sort']
        print(sort)
        DishViewList.queryset = Dish.objects.all().order_by(sort)
        return super().form_valid(form_class)


class AddDelDish(FormView):
    form_class = AddDishForm
    template_name = 'dishes/dishes_add_form.html'
    success_url = '/order/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_dish'] = Dish.objects.all()
        context['list_instance_dish'] = InstanceDish.objects.all()
        return context

    def get_queryset(self, *args, **kwargs):
        return Dish.objects.all()

    def form_valid(self, form):
        dish = Dish.objects.get(id=form.cleaned_data.get('dish_id'))
        id = form.cleaned_data.get('dish_id')
        instance_dish = InstanceDish.objects.filter(dish_template=id)
        count = form.cleaned_data.get('count')
        if instance_dish:
            instance_dish = InstanceDish.objects.get(dish_template=id)
            instance_dish.count += count
            instance_dish.save()
        else:
            instance_dish = dish.create_instance_dish(count)
        if not self.request.user.is_authenticated:
            order = Order.objects.create(user=None, full_price=0)
        else:
            order, created = Order.objects.get_or_create(user=self.request.user)
            order.dishes.add(instance_dish)
        order.get_full_price()
        return super().form_valid(form)

    # def edit_count_dish_in_order(request,pk):
    #     order = Order.objects.first()
    #     dish = order.dishes.get(id =pk)
    #     print(dish.count)
    #     print(request.POST.get('count'))
    #     # dish.count = count
    #     print ("{}".format(dish.count))
    #     order.get_full_price()
    #     return HttpResponseRedirect("/order")


class CountDish(FormView):
    form_class = CountForm
    template_name = 'dishes/dishes_add_form.html'
    success_url = '/order/'

    def form_valid(self, form):
        dish = Dish.objects.get(id =form.cleaned_data.get('dish_id'))
        print(dish.count)
        new_count = form.cleaned_data.get('count')
        print(new_count)
        instance_dish = dish.update(new_count)
        order = Order.objects.get(user=self.request.user)
        order.dishes.update(instance_dish)
        order.get_full_price()
        return super().form_valid(form)


class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer






