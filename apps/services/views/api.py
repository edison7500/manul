from rest_framework import generics
from apps.services.serializers import ServiceSerializer
from apps.services.models import Service


class ServiceListAPIView(generics.ListCreateAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()
