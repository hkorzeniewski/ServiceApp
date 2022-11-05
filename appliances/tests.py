import imp
from urllib import response
from django.test import TestCase
from rest_framework.test import APITestCase, APIClient

from users.models import User
from users.serializers import UserSerializer
# Create your tests here.


class BaseTestCase(APITestCase):

    def setUp(self):
        self.username = 'testuser'
        self.email = 'test@user.com'
        self.password = 'testuser1234'
        self.user = User.objects.create_user(
            self.username, self.email, self.password)

        self.data = {
            'username': self.username,
            'password': self.password
        }
        self.client = APIClient(enforce_csrf_checks=True)
        self.response = self.client.post(
            'http://127.0.0.1:8000/api/token/', self.data)
        self.access_token = self.response.data['access']

class TestAppliance(BaseTestCase):
    
    def test_unauthenticated_can_see_appliance_list(self):
        
        response = self.client.get("http://127.0.0.1:8000/appliances/")
        assert response.status_code == 401
    
    def test_authenticated_can_see_appliance_list(self):
       
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.get("http://127.0.0.1:8000/appliances/")
        self.assertEqual(response.status_code, 200)


class AddApplianceTest(BaseTestCase):
    
    def setUp(self):
        self.user_id = 1
        self.username = 'testuser1'
        self.email = 'test@user.com'
        self.password = 'testuser1234'
        self.user = User.objects.create_user(self.username, self.email, self.password)
        self.user_serializer = UserSerializer(self.user)
        self.data_appliance = {
            'name': 'testappliance',
            'serial_number': 'test123',
            'description': 'test description',
            'creator': 1
        }
        return super().setUp()

    def test_unauthenticated_can_see_add_page(self):
        response = self.client.get("http://127.0.0.1:8000/appliances/add/")
        assert response.status_code == 401
    
    def test_authenticated_can_see_add_page(self):
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.get("http://127.0.0.1:8000/appliances/add/")
        assert response.status_code == 200

    def test_authenticated_can_add_appliance(self):
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.post("http://127.0.0.1:8000/appliances/add/", self.data, format='json')
        assert response.status_code == 403

    def test_admin_can_add_appliance(self):
        self.user.is_admin = True
        self.user.is_staff = True
        self.user_id = 1
        self.user.save()
        self.response = self.client.post(
            'http://127.0.0.1:8000/api/token/', self.data)
        new_access_token = self.response.data['access']
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {new_access_token}')
        response = self.client.post(
            "http://127.0.0.1:8000/appliances/add/", self.data_appliance, format='json')
        print(self.data_appliance)
        assert response.status_code == 200
