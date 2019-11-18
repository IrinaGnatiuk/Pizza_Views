from django.forms import ModelForm, Form
from dishes.models import Ingredient, Drink, Dish, SortDish
from django import forms


class IngredientForm(ModelForm):
    name = forms.CharField(required=True, max_length=15)
    price = forms.DecimalField(required=True, max_digits=2)

    class Meta:
        model = Ingredient
        fields = ['name', 'is_vegan', 'is_meat', 'price']


class DrinkForm(ModelForm):
    class Meta:
        model = Drink
        fields = ['name', 'price']


class DishForm(ModelForm):
    class Meta:
        model = Dish
        fields = ['name', 'price']


class ChangePriceForm(Form):
    change_price = forms.DecimalField(required=True, max_digits=2)


class SortForm(ModelForm):
    class Meta:
        model = SortDish
        fields = ['sort']





