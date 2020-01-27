from django.shortcuts import render
from dishes.models import Dish, DishImage, DrinkImage
from django.views.generic import ListView, View, TemplateView, FormView


def all_dish(request):
    return {'all_dishes': Dish.objects.all}


def dish_img(request):
    dishes_img = DishImage.objects.filter(
        is_active=True,
        is_main=True,
        dish__is_active=True
    )
    dishes_img_sushi = dishes_img.filter(dish__category__id=1)
    dishes_img_pizza = dishes_img.filter(dish__category__id=2)
    return {'dishes_img': dishes_img,
            'dishes_img_sushi': dishes_img_sushi,
            'dishes_img_pizza': dishes_img_pizza,
            }


def drink_img(request):
    drinks_img = DrinkImage.objects.filter(
        is_active=True,
        is_main=True,
        drink__is_active=True
    )
    return {'drinks_img': drinks_img}
