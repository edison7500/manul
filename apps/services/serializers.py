from rest_framework import serializers
from apps.services.models import ServiceType, Service


class ServiceTypeSerializer(serializers.ModelSerializer):
    vendor = serializers.CharField(source="get_vendor_display")
    service = serializers.CharField(source="get_service_display")

    class Meta:
        model = ServiceType
        fields = "__all__"


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"
