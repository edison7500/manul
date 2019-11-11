import logging

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.services.models import ServiceType, Service
from apps.services.serializers import (
    ServiceSerializer, ServiceTypeSerializer, SMSSerializer, SMSVerifiedSerializer
)

logger = logging.getLogger("django")


class ServiceTypeListAPIView(generics.ListAPIView):
    serializer_class = ServiceTypeSerializer
    queryset = ServiceType.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]


class ServiceTypeDetailAPIView(generics.RetrieveAPIView):
    serializer_class = ServiceTypeSerializer
    queryset = ServiceType.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]


class ServiceListAPIView(generics.ListCreateAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)


class ServiceDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()

    def get_serializer(self, *args, **kwargs):
        if self.request.method.lower() == "post":
            _obj = self.get_object()
            if _obj.type.service == ServiceType.Service.sms:
                return SMSSerializer(**kwargs)
        return super().get_serializer(*args, **kwargs)

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        logger.info(instance)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def options(self, request, *args, **kwargs):
        _obj = self.get_object()
        return Response(data=_obj.type.options)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        _obj = self.get_object()
        r = serializer.send_sms(service=_obj)
        return Response(data=r)


class SMSVerifiedAPIView(generics.GenericAPIView):
    queryset = Service.objects.all()
    serializer_class = SMSVerifiedSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)

    def preform_send_sms(self, serializer, service):
        r = serializer.send_sms(service=service)
        return r

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        _data = self.preform_send_sms(serializer, service=self.get_object())
        return Response(data=_data, status=status.HTTP_200_OK)
