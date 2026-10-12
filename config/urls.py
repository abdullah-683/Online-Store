from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from core.views import health

admin.site.site_header = "Marketplace Admin"
admin.site.site_title = "Marketplace Admin"

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path("health/", health, name="health"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
