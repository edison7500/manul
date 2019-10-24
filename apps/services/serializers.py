from rest_framework import serializers
from drf_yasg.utils import swagger_serializer_method
from apps.services.models import ServiceType, Service


class ServiceTypeSerializer(serializers.ModelSerializer):
    vendor = serializers.CharField(source="get_vendor_display")
    service = serializers.CharField(source="get_service_display")

    class Meta:
        model = ServiceType
        fields = "__all__"


class ServiceSerializer(serializers.ModelSerializer):
    service_type = serializers.SerializerMethodField()

    class Meta:
        model = Service
        fields = "__all__"
        extra_kwargs = {
            "app_key": {"write_only": True},
            "app_secret": {"write_only": True},
            "user_id": {"write_only": True},
            "type": {"write_only": True},
        }

    @swagger_serializer_method(serializer_or_field=serializers.CharField)
    def get_service_type(self, obj):
        return "{} - {}".format(obj.type.get_vendor_display(), obj.type.get_service_display())
