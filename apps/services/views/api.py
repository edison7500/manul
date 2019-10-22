from rest_framework import generics
from rest_framework.response import Response
from django_filters import rest_framework as filters
from apps.services.serializers import ServiceSerializer, ServiceTypeSerializer
from apps.services.models import ServiceType, Service
from apps.services.filters import ServiceFilter


class ServiceTypeListAPIView(generics.ListAPIView):
    serializer_class = ServiceTypeSerializer
    queryset = ServiceType.objects.all()


class ServiceTypeDetailAPIView(generics.RetrieveAPIView):
    serializer_class = ServiceTypeSerializer
    queryset = ServiceType.objects.all()


class ServiceListAPIView(generics.ListCreateAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ServiceFilter


class ServiceDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()

    def get_queryset(self):
        return super().get_queryset()

    def options(self, request, *args, **kwargs):
        _obj = self.get_object()
        return Response(data={"msg": "ok"})
