from django.urls import path
from . import views


urlpatterns = [
    path('', views.sayHello),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('registry/', views.registry, name='registry'),
    path('devices/', views.devices, name='devices'),
    path('stats/', views.stats, name='stats'),
    path('tech/', views.tech, name='tech'),

]
