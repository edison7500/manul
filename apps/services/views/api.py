from rest_framework import generics
from apps.services.serializers import ServiceSerializer


class ServiceListAPIView(generics.ListCreateAPIView):
    serializer_class = ServiceSerializer
