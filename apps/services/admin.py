from django.contrib import admin
from apps.services.models import ServiceType, Service, SMSVerifyCode


class ServiceTypeAdmin(admin.ModelAdmin):
    list_display = ["title", "vendor", "service"]
    list_filter = ["vendor", "service"]


class ServiceAdmin(admin.ModelAdmin):
    list_display = ["title", "type", "created_at", "updated_at"]


class SMSVerifyCodeAdmin(admin.ModelAdmin):
    pass


admin.site.register(ServiceType, ServiceTypeAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(SMSVerifyCode, SMSVerifyCodeAdmin)
