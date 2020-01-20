from django.shortcuts import render
from django.views.generic import TemplateView
from dishes.cache import get_client_ip


class HomeView(TemplateView):

    def get(self, request, *args, **kwargs):
        get_client_ip(request)
        return render(request, 'home.html')
