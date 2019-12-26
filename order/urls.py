from django.conf.urls import url, include
from django.urls import path
from . import views
from order.views import MakeOrder

urlpatterns = [
    # path('orders/', views.OrderView.as_view()),
    # path('orders/', views.MyView.as_view()),
    path('order/', views.OrderView.as_view()),
    path('del_dish/<int:pk>/', views.OrderView.del_dish_from_order, name='delete_dish_from_order'),
    # path('edit_count/<int:pk>/', views.OrderView.edit_count_dish_in_order, name='edit_count_dish_in_order'),
    # path('orders/new/', views.MakeOrder.as_view()),
]