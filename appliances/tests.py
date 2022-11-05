import imp
from urllib import response
from django.test import TestCase
from rest_framework.test import APITestCase, APIClient

from users.models import User
# Create your tests here.

class TestAppliance(TestCase):
    
    def setUp(self):
        self.username = 'testuser'
        self.email = 'test@user.com'
        self.password = 'testuser1234'
        self.user = User.objects.create_user(
            self.username, self.email, self.password)
        self.client = APIClient(enforce_csrf_checks=True)
        self.data = {
            'username': self.username,
            'password': self.password
        }

    def test_unauthenticated_can_see_appliance_list(self):
        
        response = self.client.get("http://127.0.0.1:8000/appliances/")
        assert response.status_code == 401
    
    def test_authenticated_can_see_appliance_list(self):
        response = self.client.post('http://127.0.0.1:8000/api/token/', self.data)
        token_access = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token_access}')
        response = self.client.get("http://127.0.0.1:8000/appliances/")
        self.assertEqual(response.status_code, 200)

    