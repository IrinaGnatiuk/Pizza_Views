from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings
from celery.decorators import task
# from dishes.models import Dish, InstanceDish
# from dishes.views import AddDish
# from order.models import Order
# from django.views.generic.edit import FormView

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
app = Celery('project')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


@task(name="sum_two_numbers")
def add(x, y):
    print(x + y)
