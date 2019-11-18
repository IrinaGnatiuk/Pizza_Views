from django.shortcuts import render
from django.views.generic import ListView, View, TemplateView
from django.views.generic.edit import FormView, UpdateView
from dishes.models import Dish, Drink, Ingredient
from django.http import HttpResponse
from .forms import IngredientForm, DrinkForm, DishForm


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
    queryset = Drink.objects.order_by("name")
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
    queryset = Dish.objects.order_by("name")
    context_object_name = 'dishes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_var'] = 'DishesListView'
        return context

    def get_quertyset(self, *args, **kwargs):
        return Dish.objects.all()


class IngredientViewList(ListView):
    model = Ingredient
    template_name = 'dishes/ingredient_list.html'
    queryset = Ingredient.objects.order_by("name")
    context_object_name = 'ingredients'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_var'] = 'IngredientListView'
        return context

    def get_quertyset(self, *args, **kwargs):
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
