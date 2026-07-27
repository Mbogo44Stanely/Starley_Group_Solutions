from django.contrib import admin

from .models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_published', 'is_featured', 'order', 'updated_at']
    list_editable = ['is_published', 'is_featured', 'order']
    list_filter = ['is_published', 'is_featured']
    search_fields = ['title', 'summary', 'description']
    prepopulated_fields = {'slug': ('title',)}
