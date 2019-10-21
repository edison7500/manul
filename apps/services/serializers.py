from rest_framework import serializers
from apps.services.models import Service


class ServiceSerializer(serializers.ModelSerializer):

    content_json = serializers.JSONField()

    class Meta:
        model = Service
        # fields = "__all__"
        exclude = ["content", ]
