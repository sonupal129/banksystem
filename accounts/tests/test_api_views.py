from rest_framework.test import APIClient
from django.test import TestCase
from rest_framework import status
from django.urls import reverse
# CODE BELOW

class BankingAPIViewTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.data = {
                    "account_number": 19261870,
                    "transaction_type": "CR",
                    "amount": "55.00"
                    }
        self.response = self.client.post(reverse("banking"), self.data, format="json")

    
    def test_api_response(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)