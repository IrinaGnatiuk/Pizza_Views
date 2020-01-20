from django.conf.urls import url, include
from django.urls import path
from . import views
# from order.views import MakeOrder

urlpatterns = [
    # path('orders/', views.OrderView.as_view()),
    # path('orders/', views.MyView.as_view()),
    path('order/', views.OrderView.as_view(), name='order'),
    path('order/shipping_form', views.MakeShippingOrderForm.as_view(), name='shipping_form'),
    path('del_dish/<int:pk>/', views.OrderView.del_dish_from_order, name='delete_dish_from_order'),
    # path('change_count/<int:pk>/', views.OrderView.edit_count_dish, name='edit_count_dish'),
    path('change_count/<int:pk>/', views.EditCountDish.as_view(), name='edit_count_dish'),
    # path('edit/<int:pk>/', views.MakeOrder.edit_count_dish, name='edit_count_dish_in_order'),
    # path('orders/new/', views.MakeOrder.as_view()),
]