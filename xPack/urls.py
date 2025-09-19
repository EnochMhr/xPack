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
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('xPack_App/', include('xPack_App.urls')),
    path('xPack_Registrar/', include('xPack_Registrar.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='registrar/login.html'), name='user-login'),
    path('logout/', auth_views.LogoutView.as_view(), name='user-logout'),
]
