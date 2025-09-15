from django.urls import path, include

urlpatterns = [
    path('admin/', include('xPack_App.urls.admin_urls')),
    path('registrar/', include('xPack_App.urls.registrar_urls'))
]
