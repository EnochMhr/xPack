from django.contrib import admin
from .models import Registrar, AdminCredentials

@admin.register(AdminCredentials)
class AdminCredentialsAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_active', 'last_modified')
    list_filter = ('is_active', )
    search_fields = ('user__username', )
    
@admin.register(Registrar)
class RegistrarAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'created_at')
    search_fields = ('name', 'contact')