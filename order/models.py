from django.db import models
from dishes.models import Dish, Drink

# Create your models here.


class Order(models.Model):
    dishes = models.ManyToManyField(Dish, blank=True)
    drinks = models.ManyToManyField(Drink, blank=True)
    date_created = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    place_delivery = models.CharField(max_length=512)
    user_profile = models.CharField(max_length=512)

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'

    def save(self, *args, **kwargs):
        price_dishes = sum([dish.price for dish in self.dishes.all()])
        price_drinks = sum([drink.price for drink in self.drinks.all()])
        self.price = price_dishes + price_drinks
        super().save(*args, **kwargs)