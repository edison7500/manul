from rest_framework import generics
from apps.services.serializers import ServiceSerializer, ServiceTypeSerializer
from apps.services.models import ServiceType, Service


class ServiceTypeListAPIView(generics.ListAPIView):
    serializer_class = ServiceTypeSerializer
    queryset = ServiceType.objects.all()


class ServiceTypeDetailAPIView(generics.RetrieveAPIView):
    serializer_class = ServiceTypeSerializer
    queryset = ServiceType.objects.all()


class ServiceListAPIView(generics.ListCreateAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()


class ServiceDetailAPIView(generics.RetrieveAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()
