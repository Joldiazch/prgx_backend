#django
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
# rest framework
from rest_framework.test import APIClient
from rest_framework import status

class ExtractApiTestCase(TestCase):

    def setUp(self):
        # api client
        self.client = APIClient()


    def test_extract_url(self):
        """
        test if /extract/ endpoint is work
        """
        url = reverse('extract')
        response = self.client.get(url)
        print(status.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)