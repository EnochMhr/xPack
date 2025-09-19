from django.urls import path
from . import views


urlpatterns = [
    # path('', views.base, name='base'),
    path('dashboard/', views.reg_dashboard, name='reg_dashboard'),
    path('family/', views.family, name='family'),
    path('packages/', views.packages, name='packages'),
    path('served/', views.served, name='served'),
    path('reg_tech/', views.reg_tech, name='reg_tech'),
    path('new_entry/', views.new_entry, name='new_entry'),
    path('family_entry/', views.family_entry, name='family_entry'),
]
