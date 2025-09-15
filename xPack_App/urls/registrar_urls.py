from django.urls import path
from ..views import registrar_view

urlpatterns = [
    path('', registrar_view.dashboard, name='registrar_dashboard'),
    path('devices/', registrar_view.devices, name='registrar_devices'),
    path('profile/', registrar_view.profile, name='registrar_profile'),
    path('reports/', registrar_view.reports, name='registrar_reports'),
]