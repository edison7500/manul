from rest_framework import serializers
from apps.services.models import ServiceType, Service


class ServiceTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServiceType
        fields = "__all__"


class ServiceSerializer(serializers.ModelSerializer):

    content_json = serializers.JSONField()

    class Meta:
        model = Service
        # fields = "__all__"
        exclude = ["content", ]
