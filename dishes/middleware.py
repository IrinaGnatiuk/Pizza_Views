from django.utils.deprecation import MiddlewareMixin
import time
from django.contrib.auth import logout


class UserlogOutMiddleware(MiddlewareMixin):
    def process_request(self, request):
        current_time = time.time()
        log_user_time = request.session.get('log_user_time')
        request.session['log_user_time'] = current_time

        if request.user.is_authenticated:
            logout_time = current_time - log_user_time
            if logout_time > 60:
                logout(request)
            else:
                request.session['log_user_time'] = current_time

    def process_response(self, request, response):
        return response
