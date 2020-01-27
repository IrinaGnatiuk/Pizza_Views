from django.core.cache import cache


def get_client_ip(request):

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    if cache.get('ip') != ip:
        message = 'ИЗМЕНИЛСЯ ip  стал: '
        cache.set('ip', ip, 60*5)
    else:
        message = 'ip БЕЗ ИЗМЕНЕНИЙ :'
    return print(message, ip)
