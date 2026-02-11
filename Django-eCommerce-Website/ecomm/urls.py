from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from ecomm import error_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('product/', include('products.urls')),
    path('accounts/', include('accounts.urls')),
    path("accounts/", include("allauth.urls")),
]

# Custom error handlers (work when DEBUG=False)
handler404 = error_views.custom_404
handler500 = error_views.custom_500


if settings.DEBUG:
    # Preview pages for custom templates while developing
    urlpatterns += [
        path("__404__/", error_views.preview_404),
        path("__500__/", error_views.preview_500),
    ]
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()
