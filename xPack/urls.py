"""
URL configuration for xPack project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from xPack_App.auth_views import custom_login, custom_logout
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),  # Keep original admin URL
    path('xPack_App/', include('xPack_App.urls')),
    path('xPack_Registrar/', include('xPack_Registrar.urls')),
    path('', custom_login, name='login'),  # Custom login view as root URL
    path('logout/', custom_logout, name='logout'),  # Use our custom logout view
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
