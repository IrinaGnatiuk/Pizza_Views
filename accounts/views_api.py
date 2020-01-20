from django.views.generic.base import View
from django.shortcuts import redirect, render_to_response, reverse, render
from django.http import JsonResponse
from .models import User


class UsersApiView(View):

    def get(self, request):
        # users = list(User.objects.all().values_list('email', flat=True))
        sort = request.GET.get('sort')
        users = User.objects.all()
        if sort:
            users = User.objects.all().order_by(sort)
        serialize_users = []
        for user in users:
            serialize_users.append(user.get_serialize_users())
        return JsonResponse({'users_list': serialize_users})


class CreateUsersApiView(View):

    def get(self, request):
        return JsonResponse({'message': "method GET not supported. Please use POST"})

    def post(self,request, *args, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create(email=email, username=email)
        user.set_password(password)
        user.save()
        return JsonResponse({'message': " User created",
                             "user": user.get_serialize_users()
        })


