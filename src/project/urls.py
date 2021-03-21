"""
==============
     URLs
==============
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from apps.homepage.views import homepage
from apps.sobre.views import sobre
from apps.diretoria.views import diretoria
from apps.expresidentes.views import expresidentes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    path('about', sobre),
    path('diretoria', diretoria),
    path('ex-presidentes', expresidentes)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
