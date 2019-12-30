from django.test import Client, TestCase
from django.urls import resolve, reverse
from .models import Dish


class Test(TestCase):

    def setUp(self):
        Dish.objects.create(name='dish1', price=90)

    #
    # def setUpTestData(cls):
    #     Dish.objects.create(name='dish_one', price=90)
    #     Dish.objects.create(name='dish_two', price=300)

    def test_dish(self):
        dish = Dish.objects.get(id=1)
        field_label = dish._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_view_success_status_code(self):
        url = reverse('update_dish', kwargs={'pk': 1})
        # self.assertEquals(url, '/dishes/1/edit/')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_not_found_status_code(self):
        url = reverse('update_dish', kwargs={'pk': 2})
        # self.assertEquals(url, '/dishes/99/edit/')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    # def test_url_resolves_update_dish_view(self):
    #     view = resolve('/dishes/list')
    #     self.assertEquals(view.func, board_topics)
