import factory
from faker import Faker
from apps.services.models import ServiceType

f = Faker()


class ServiceTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ServiceType
    vendor = ServiceType.Vendor.aliyun
    service = ServiceType.Service.sms
