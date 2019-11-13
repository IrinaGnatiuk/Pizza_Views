from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [
    path('orders/', views.OrderView.as_view()),
    path('orders/', views.MyView.as_view()),
    path('orders/', views.AboutView.as_view()),

]