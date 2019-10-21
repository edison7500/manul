from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from rest_framework import status


class ServiceAPITestCase(APITestCase):

    def test_create_a_service_view(self):
        _url = reverse("api:services:index")

    def test_get_service_list_view(self):
        _url = reverse("api:services:index")
        res = self.client.get(_url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
