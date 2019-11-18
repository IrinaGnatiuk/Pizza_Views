from django.db import models


class BaseItem(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=9, decimal_places=2, default=0)

    class Meta:
        abstract = True


class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    is_vegan = models.BooleanField(default=False)
    is_meat = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=9, decimal_places=2, default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'


class Dish(BaseItem):
    ingredients = models.ManyToManyField(Ingredient, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'


class Drink(BaseItem):
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Напиток'
        verbose_name_plural = 'Напитки'


class ChangePrice(models.Model):
    change_price = models.DecimalField(max_digits=9, decimal_places=2, default=0)


class SortDish(models.Model):
    FILTER_TYPES = (
        ('price+', 'price по возрастанию'),
        ('price-', 'price по убыванию'),
        ('name+', 'name по возрастанию'),
        ('name-', 'name убыванию'),
    )
    sort = models.CharField(max_length=15, choices=FILTER_TYPES, default='price +')
