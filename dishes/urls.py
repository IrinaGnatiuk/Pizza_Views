from django.conf.urls import url, include
from django.urls import path
from .views import *

urlpatterns = [
    path('dishes/', DishView.as_view()),
    path('', StartView.as_view()),
    path('ingredients/', IngredientView.as_view()),
    path('drinks/', DrinkView.as_view()),
    path('dishes/list', DishViewList.as_view()),
    path('ingredients/list', IngredientViewList.as_view()),
    path('ingredients/new/', MakeIngredient.as_view(), name='ingredient_form'),
    path('drinks/new/', MakeDrink.as_view(), name='drinks_form'),
    path('dishes/new/', MakeDishes.as_view(), name='dishes_form'),
    path('drinks/<int:pk>/edit/', UpdateDrink.as_view(), name='update_drink'),
    path('ingredients/<int:pk>/edit/', UpdateIngredient.as_view(), name='update_ingredient'),
    path('dishes/<int:pk>/edit/', UpdateDish.as_view(), name='update_dish')
]
