import json
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from faker import Faker
from pprint import pprint
from .faker_data import ServiceTypeFactory

f = Faker()


class ServiceAPITestCase(APITestCase):

    # def test_create_a_service_type_view(self):
    #     _url = reverse()
    def setUp(self) -> None:
        self.st = ServiceTypeFactory()

    def test_create_a_service_view(self):
        _url = reverse("api:services:index")
        payload = {
            "user_id": f.pyint(),
            "type": self.st.id,
            "app_key": f.pystr(),
            "app_secret": f.md5(),
            "title": f.name(),
            "content": {"TemplateName": f.name()}
        }
        res = self.client.post(_url, data=payload, format="json")
        # pprint(res.content)
        # pprint(json.loads(res.content))
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_get_service_list_view(self):
        _url = reverse("api:services:index")
        res = self.client.get(_url, follow="json")
        self.assertEqual(res.status_code, status.HTTP_200_OK)
