from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),

    path('user/', include('users.urls')),

    path('', include('filter.urls')),
    
    path('vendor/', include('vendors.urls')),

    path('cart/', include('cart.urls')),

    path('orders/', include('orders.urls')),

    path('mail/', include('mail.urls')),

    path('share/', include('share.urls'))
]

handler404 = "core.views.page_not_found_view"


if settings.DEBUG:
        import debug_toolbar

        urlpatterns = [
            path('__debug__/', include('debug_toolbar.urls')),
        ] + urlpatterns
        urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

