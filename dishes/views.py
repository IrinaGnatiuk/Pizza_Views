from django.shortcuts import render
from django.views.generic import ListView, View, TemplateView
from django.views.generic.edit import FormView, UpdateView
from dishes.models import Dish, Drink, Ingredient, ChangePrice, SortDish
from django.http import HttpResponse
from .forms import IngredientForm, DrinkForm, DishForm, ChangePriceForm, SortForm


class DishView(TemplateView):
    model = Dish
    context_object_name = 'dish'
    template_name = 'dishes/dishes.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_var'] = 'DishTemplateView'
        return context


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
        context['list_dish2'] = Dish.objects.values_list('name',flat=True).order_by('price')
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
    success_url = '/'
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
    success_url = '/'


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
        for price in Dish.objects.values_list('price',flat=True):
            new_price =  price + change_price
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
        if sort == 'price+':
            DishViewList.queryset = Dish.objects.all().order_by('price')
        elif sort == 'price-':
            DishViewList.queryset = Dish.objects.all().order_by('-price')
        elif sort == 'name+':
            DishViewList.queryset = Dish.objects.all().order_by('name')
        else:
            DishViewList.queryset = Dish.objects.all().order_by('-name')
        return super().form_valid(form_class)
