from django.urls import path
from . import views


urlpatterns = [
        # use this path by giving an empty string in the urls path of the main project
        # so that on load of the local host you go staight to the dashboard
    # path('', views.dashboard, name='dashboard'), 
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('registry/', views.registry, name='registry'),
    path('devices/', views.devices, name='devices'),
    path('stats/', views.stats, name='stats'),
    path('tech/', views.dash_tech, name='dash_tech'),
    path('add/', views.add, name='add'),
    path('delete_registrar/<int:id>/', views.delete_registrar, name='delete_registrar'),
    path('update_registrar/<int:id>/', views.update_registrar, name='update_registrar')

]
 