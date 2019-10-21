import factory
from faker import Faker
from apps.services.models import ServiceType, Service

f = Faker()


class ServiceTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ServiceType
    vendor = factory.Iterator([ServiceType.Vendor.aliyun, ServiceType.Vendor.tencent])
    service = ServiceType.Service.sms


class ServiceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Service
    user_id = f.pyint()
    type = factory.SubFactory(ServiceTypeFactory)
    app_key = f.pystr()
    app_secret = f.md5()
    title = f.name()


