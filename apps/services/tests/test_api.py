from faker import Faker
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from apps.account.tests.faker_data import UserFactory
from .faker_data import ServiceTypeFactory, ServiceFactory

f = Faker()


class ServiceTypeAPITestCase(APITestCase):

    def setUp(self) -> None:
        self.st = ServiceTypeFactory()

    def test_get_service_type_list_view(self):
        _url = reverse("api:types:index")
        res = self.client.get(_url, format="json")
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_get_a_service_type_view(self):
        _url = reverse("api:types:detail", args=[self.st.pk])
        res = self.client.get(_url, format="json")
        self.assertEqual(res.status_code, status.HTTP_200_OK)


class ServiceAPITestCase(APITestCase):

    def setUp(self) -> None:
        self.user = UserFactory()
        self.st = ServiceTypeFactory()
        self.service = ServiceFactory(
            user=self.user
        )
        self.token = Token.objects.create(user=self.user)

    def test_create_a_service_view(self):
        _url = reverse("api:services:index")
        payload = {
            "type": self.st.id,
            "app_key": f.pystr(),
            "app_secret": f.md5(),
            "title": f.name(),
            "content": {"TemplateName": f.name()}
        }
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        res = self.client.post(_url, data=payload, format="json")
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_get_service_list_view(self):
        _url = reverse("api:services:index")
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        res = self.client.get(_url, follow="json")
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_get_service_detail_view(self):
        _url = reverse("api:services:detail", args=[self.service.pk])
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        res = self.client.get(_url, format="json")
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_update_service_view(self):
        _url = reverse("api:services:detail", args=[self.service.pk])
        payload = {
            "type": self.st.id,
            "app_key": f.pystr(),
            "app_secret": f.md5(),
            "title": f.name(),
            "content": {"TemplateName": f.name()}
        }
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        res = self.client.put(_url, data=payload, format="json")
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_patch_service_view(self):
        _url = reverse("api:services:detail", args=[self.service.pk])
        payload = {
            "app_key": f.pystr(),
            "app_secret": f.md5(),
            "title": f.name(),
            "content": {"TemplateName": f.name()}
        }
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        res = self.client.patch(_url, data=payload, format="json")
        self.assertEqual(res.status_code, status.HTTP_200_OK)
