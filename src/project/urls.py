"""
==============
     URLs
==============
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from pages.views import home_view, about_view, diretoria_view, expresidentes_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),  # Home
    path('about', about_view),
    path('diretoria', diretoria_view),
    path('ex-presidentes', expresidentes_view)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
