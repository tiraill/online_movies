from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('billing/admin/', admin.site.urls),
    path('billing/demo/', include('demo.urls')),
    path('billing/subscription/', include('billing.apps.subscriptions.api.urls')),
]

if settings.DEBUG:
    import debug_toolbar  # type: ignore # noqa
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns  # type: ignore # noqa

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
    urlpatterns += staticfiles_urlpatterns()  # type: ignore
