from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from django.views.decorators.cache import cache_page
from project.views import HomeView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', TemplateView.as_view(template_name="index.html")),
    path('', cache_page(60*10)(HomeView.as_view(template_name="home.html"))),
    path('accounts/', include('accounts.urls')),
    path('', include('core.urls')),
    path('', include('dishes.urls')),
    path('', include('order.urls')),
    path('', include('accounts.urls')),
]

if settings.DEBUG:
    urlpatterns += [
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += [
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]

urlpatterns += staticfiles_urlpatterns()
