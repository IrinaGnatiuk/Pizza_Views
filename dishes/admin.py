from django.contrib import admin
from dishes.models import Dish, Drink,  Ingredient, InstanceDish, DishImage, \
    DishCategory, DrinkImage


class DishCategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in DishCategory._meta.fields]

    class Meta:
        model = DishCategory


class DishImageInline(admin.TabularInline):
    model = DishImage
    extra = 0
# количество дополнительных полей с возможностью добавления картинок
# по умолчанию в админке блюда


class DrinkImageInline(admin.TabularInline):
    model = DrinkImage
    extra = 0


class DishAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']
    inlines = [DishImageInline]

    class Meta:
        model = Dish


class DishImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in DishImage._meta.fields]

    class Meta:
        model = DishImage


class DrinkAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    inlines = [DrinkImageInline]

    class Meta:
        model = Drink


class DrinkImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in DrinkImage._meta.fields]

    class Meta:
        model = DrinkImage


admin.site.register(DishCategory, DishCategoryAdmin)
admin.site.register(DishImage, DishImageAdmin)
admin.site.register(Dish, DishAdmin)
admin.site.register(Drink, DrinkAdmin)
admin.site.register(DrinkImage, DrinkImageAdmin)
admin.site.register(Ingredient)
admin.site.register(InstanceDish)
