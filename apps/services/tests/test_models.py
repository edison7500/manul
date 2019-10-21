from django.test import TestCase
from apps.services.models import ServiceType


class TestServiceTypeModelTestCase(TestCase):

    def setUp(self) -> None:
        self.count = ServiceType.objects.count()

    def test_create_a_service_type(self):
        ServiceType.objects.create(
            vendor=ServiceType.Vendor.aliyun,
            service=ServiceType.Service.sms,
        )

        new_count = ServiceType.objects.count()

        self.assertGreater(new_count, self.count)



