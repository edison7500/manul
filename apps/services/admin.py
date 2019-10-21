from django.contrib import admin
from apps.services.models import ServiceType, Service


class ServiceTypeAdmin(admin.ModelAdmin):
    list_display = ["title", "vendor", "service"]


class ServiceAdmin(admin.ModelAdmin):
    pass


admin.site.register(ServiceType, ServiceTypeAdmin)
admin.site.register(Service, ServiceAdmin)