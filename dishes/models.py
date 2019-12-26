from django.db import models


class BaseItem(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
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


class Dish(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    # ingredients = models.ManyToManyField(Ingredient, blank=True)

    def __str__(self):
        return self.name

    def create_instance_dish(self, count):
        return InstanceDish.objects.create(
            name=self.name,
            price=self.price,
            dish_template=self,
            count=count
        )

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
    change_price = models.DecimalField(
        max_digits=9, decimal_places=2, default=0
    )


class SortDish(models.Model):
    FILTER_TYPES = (
        ('price', 'price по возрастанию'),
        ('-price', 'price по убыванию'),
        ('name', 'name по возрастанию'),
        ('-name', 'name убыванию'),
    )
    sort = models.CharField(
        max_length=15, choices=FILTER_TYPES, default='price +'
    )


class InstanceDish(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    count = models.PositiveSmallIntegerField(default=1)
    dish_template = models.ForeignKey(
        Dish, related_name="dish_templates", blank=True, null=True,
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return 'name: {}, price {},  full_price: {}  '\
            .format(self.name, str(self.price), str(self.price * self.count))

    def all_price_dish(self):
        all_price = self.price * self.count
        return all_price
