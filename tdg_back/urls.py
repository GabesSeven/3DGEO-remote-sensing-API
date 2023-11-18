from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView, TokenBlacklistView


"""
URL da aplicação "authentication"
"""
urlpatterns = [] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

""" 
Configuração para servir arquivos estáticos durante o desenvolvimento.
"""
urlpatterns += staticfiles_urlpatterns()