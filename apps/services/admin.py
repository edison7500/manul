from django.contrib import admin
from apps.services.models import ServiceType


class ServiceTypeAdmin(admin.ModelAdmin):
    pass


admin.site.register(ServiceType, ServiceTypeAdmin)
