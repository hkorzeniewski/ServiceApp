import imp
from urllib import response
from django.test import TestCase
from rest_framework.test import APITestCase, APIClient

from users.models import User
# Create your tests here.

class TestAppliance(TestCase):
    # def setUp(self):
    #     # self.superuser = User.objects.create_superuser('test', 'test@test.pl', 'testpassword')
    #     self.client =

    def test_appliance_list(self):
        client = APIClient()
        response = client.get("http://127.0.0.1:8000/appliances/")
        assert response.status_code == 200
    