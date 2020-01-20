from django.conf.urls import url, include
from django.urls import path
from .views import *
from  .views_api import *
from rest_framework import routers, serializers, viewsets

router = routers.DefaultRouter()
router.register(r'dishes', DishViewSet)

urlpatterns = [
    path('dishes/', InstanceDishView.as_view()),
    # path('', StartView.as_view(), name='start_page'),
    path('ingredients/', IngredientView.as_view()),
    path('drinks/', DrinkView.as_view()),
    path('dishes/list', DishViewList.as_view(), name='list_of_dish'),
    path('ingredients/list', IngredientViewList.as_view()),
    path('ingredients/new/', MakeIngredient.as_view(), name='ingredient_form'),
    path('drinks/new/', MakeDrink.as_view(), name='drinks_form'),
    path('dishes/new/', MakeDishes.as_view(), name='dishes_new'),
    path('dishes/add/', AddDish.as_view(), name='add_dish_to_order'),
    path('price/', CreateNewPrice.as_view(), name='new price'),
    path('sort/', MakeSort.as_view(), name='make sort'),
    path('drinks/<int:pk>/edit/', UpdateDrink.as_view(), name='update_drink'),
    path('ingredients/<int:pk>/edit/',
         UpdateIngredient.as_view(), name='update_ingredient'),
    path('dishes/<int:pk>/edit/', UpdateDish.as_view(), name='update_dish'),
    path('dishes/<int:pk>/', DishDetailView.as_view(), name='dish'),
    path('drinks/<int:pk>/', DrinkDetailView.as_view(), name='drink'),
    path('api/', include(router.urls)),
    path('api/dishes_list/', DishesApiView.as_view(), name='dishes_list_api'),
    path('api/order/', OrderApiView.as_view(), name='order_api'),
    path('api/dish/add_to_order/', DishesAddOrderApiView.as_view(), name='dish_add_to_order'),
    # path('api/', include('dishes.urls')),

]
