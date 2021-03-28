"""
==============
     URLs
==============
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from pages.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),  # Home
    path('about', about_view),
    path('diretoria', diretoria_view),
    path('ex-presidentes', expresidentes_view),
    path('eventos-anteriores', eventosanteriores_view)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
