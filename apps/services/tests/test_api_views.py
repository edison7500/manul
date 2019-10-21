from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


class ServiceAPITestCase(APITestCase):

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_service_list_api_view(self):
        _url = reverse("api:services:index")

        res = self.client.get(_url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
