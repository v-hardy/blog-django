from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

@admin.register(Usuario)
class CustomUserAdmin(UserAdmin):
    model = Usuario
    list_display = ['username', 'email', 'rol', 'is_staff', 'is_active']
    fieldsets = UserAdmin.fieldsets + (
        ('Rol personalizado', {'fields': ('rol',)}),
    )
