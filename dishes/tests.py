
from django.test import Client, TestCase
from django.urls import resolve, reverse
from .models import Dish


class TestDish(TestCase):

    def setUp(self):
        Dish.objects.create(name='dish_one', price=120)
        Dish.objects.create(name='dish_two', price=150)

    def test_dish(self):
        dish1 = Dish.objects.first()
        dish = Dish.objects.get(id=2)
        field_label = dish._meta.get_field('name').verbose_name
        field_label2 = dish._meta.get_field('price').verbose_name
        self.assertEquals(field_label, 'name')
        self.assertEquals(field_label2, 'price')
        self.assertEquals(dish1.name, 'dish_one')
        self.assertEquals(dish1.price, 120)
        self.assertEquals(dish.name, 'dish_two')
        self.assertEquals(dish.price, 150)
        self.assertTrue(dish.price > 0)

    def test_view_success_status_code_update_dish(self):
        url1 = reverse('update_dish', kwargs={'pk': 1})
        url2 = reverse('update_dish', kwargs={'pk': 2})
        self.assertEquals(url1, '/dishes/1/edit/')
        self.assertEquals(url2, '/dishes/2/edit/')
        response1 = self.client.get(url1)
        response2 = self.client.get(url2)
        self.assertEquals(response1.status_code, 200)
        self.assertEquals(response2.status_code, 200)

    def test_view_success_status_code_order(self):
        url = reverse('order')
        self.assertEquals(url, '/order/')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_view_add_dish_to_order(self):
        url = reverse('add_dish_to_order')
        self.assertEquals(url, '/dishes/add/')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(response.context['list_dish']), 2)
        self.assertTrue(len(response.context['list_dish']) == 2)

    def test_view_list_of_dish(self):
        url = reverse('list_of_dish')
        self.assertEquals(url, '/dishes/list')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(response.context['list_dish1']), 2)
        self.assertFalse(len(response.context['list_dish1']) == 5)

    def test_view_new_dish(self):
        url = reverse('dishes_new')
        self.assertEquals(url, '/dishes/new/')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_view_change_price(self):
        url = reverse('new price')
        self.assertEquals(url, '/price/')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_not_found_status_code(self):
        url = reverse('update_dish', kwargs={'pk': 99})
        self.assertEquals(url, '/dishes/99/edit/')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)
