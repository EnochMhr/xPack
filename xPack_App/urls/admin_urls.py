from django.urls import path
from ..views import admin_views


urlpatterns = [
    path('', admin_views.sayHello),
    path('dashboard/', admin_views.dashboard, name='dashboard'),
    path('registry/', admin_views.registry, name='registry'),
    path('devices/', admin_views.devices, name='devices'),
    path('stats/', admin_views.stats, name='stats'),
    path('tech/', admin_views.tech, name='tech'),
    path('add/', admin_views.add, name='add'),
    path('delete_registrar/<int:id>/', admin_views.delete_registrar, name='delete_registrar'),
    path('update_registrar/<int:id>/', admin_views.update_registrar, name='update_registrar')

]
