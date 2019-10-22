from django_filters import rest_framework as filters
from apps.services.models import Service


class ServiceFilter(filters.FilterSet):
    uid = filters.NumberFilter(field_name="user_id")

    class Meta:
        model = Service
        fields = ["uid"]
