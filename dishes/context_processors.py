from order.models import Order


def order(request):
    return {'order': Order.objects.get(user=request.user)}