from django.contrib import admin
from .models import Column, Task

@admin.register(Column)
class ColumnAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "order")
    ordering = ("order",)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "column", "order", "created_at", "updated_at")
    list_filter = ("column",)
    search_fields = ("title", "description")
    ordering = ("column", "order")
