from django.db import models
from dishes.models import Dish, Drink, InstanceDish
from accounts.models import User


class Order(models.Model):
    dishes = models.ManyToManyField(InstanceDish, blank=True)
    full_price = models.DecimalField(max_digits=9, decimal_places=2, blank=True)
    user = models.ForeignKey(User, null=True, max_length=512, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'

    def __str__(self):
        return 'Order № {}  Total price {}'. format(self.id,  self.full_price)

    def get_full_price(self):
        dishes = self.dishes.all()
        full_price = 0
        for dish in dishes:
            full_price += dish.price*dish.count
        self.full_price = full_price
        self.save()
        return full_price

    def del_dish_from_order(self, id):
        order = Order.objects.get(user=self.request.user)
        dish = order.dishes.get(id=id)
        order.remove(dish)
        order.get_full_price()
        return HttpResponseRedirect("/order")