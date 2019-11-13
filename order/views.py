from django.shortcuts import render
from django.views.generic import ListView, View, TemplateView
from order.models import Order
from django.http import HttpResponse


class OrderView(TemplateView):
    model = Order
    context_object_name = 'order'
    template_name = 'order/order.html'

    def get_context_data(self, **kwargs):
        context = super(OrderView, self).get_context_data(**kwargs)
        # context = Order.objects.filter(price__gt=50).order_by('-price')
        context['user_profile'] = Order.objects.all()
        context['my_var'] = 'TemplateView'
        return context


class AboutView(ListView):
    model = Order
    template_name = 'order/order1.html'
    queryset = Order.objects.order_by("-date_create")
    context_object_name = 'order'

    def get_quertyset(self):
        return Order.objects.all()


class MyView(View):
    model = Order
    context_object_name = 'order'
    template_name = 'order/order.html'

    def get(self, request, *args, **kwargs):
        return HttpResponse("HELLO!!!")


