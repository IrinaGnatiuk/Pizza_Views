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


class DishCategory(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Вид еды'
        verbose_name_plural = 'Виды еды'


class Dish(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    discount = models.IntegerField(blank=True, null=True, default=0)
    category = models.ForeignKey(
        DishCategory,
        blank=True, null=True,
        default=None, on_delete=models.SET_NULL
    )
    short_description = models.TextField(blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)

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

    def get_serialize_dishes(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "description": self.description,
        }

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'


class Drink(BaseItem):
    short_description = models.TextField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    discount = models.IntegerField(blank=True, null=True, default=0)

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


class DishImage(models.Model):
    dish = models.ForeignKey(
        Dish,
        blank=True, null=True,
        default=None, on_delete=models.SET_NULL
    )
    is_main = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to="dishes_images/")

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Фотография еды'
        verbose_name_plural = 'Фотографии еды'


class DrinkImage(models.Model):
    drink = models.ForeignKey(
        Drink,
        blank=True, null=True,
        default=None, on_delete=models.SET_NULL
    )
    is_main = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to="drink_images/")

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Фотография напитка'
        verbose_name_plural = 'Фотографии напитков'
