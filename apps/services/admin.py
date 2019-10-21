from django.contrib import admin
from apps.services.models import ServiceType, Service


class ServiceTypeAdmin(admin.ModelAdmin):
    list_display = ["title", "vendor", "service"]


class ServiceAdmin(admin.ModelAdmin):
    list_display = ["title", "type", "created_at", "updated_at"]


admin.site.register(ServiceType, ServiceTypeAdmin)
admin.site.register(Service, ServiceAdmin)
