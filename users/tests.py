from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient, force_authenticate
from rest_framework import status


from .models import User
from .serializers import UserSerializer, RegisterUserSerializer
from . import utils as test_utils

from rest_framework_jwt import utils, views
from rest_framework_jwt.compat import get_user_model
from rest_framework_jwt.settings import api_settings
# Create your tests here.

class BaseTestCase(APITestCase):

    def setUp(self):
        self.username = 'testuser'
        self.email = 'test@user.com'
        self.password = 'testuser1234'
        self.user = User.objects.create_user(self.username, self.email, self.password)

        self.data = {
            'username': self.username,
            'password': self.password
        }
        self.client = APIClient(enforce_csrf_checks=True)
        self.response = self.client.post('http://127.0.0.1:8000/api/token/', self.data)
        self.access_token = self.response.data['access']

 
class TestCustomResponsePayload(BaseTestCase):

    def test_jwt_login_custom_response_json(self):
        """
        Ensure JWT login view using JSON POST works.
        """

        decoded_payload = utils.jwt_decode_handler(self.response.data['access'])
        decoded_username = utils.jwt_payload_handler(self.user)
        # print(decoded_username['username'])
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        self.assertEqual(decoded_username['username'], self.username)


class ObtainJSONWebTokenTests(BaseTestCase):
    def test_jwt_login_form(self):

        decoded_username = utils.jwt_payload_handler(self.user)
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        self.assertEqual(decoded_username['username'], self.username)

    def test_jwt_login_json_bad_creds(self):
        """
        Ensure JWT login view using JSON POST fails
        if bad credentials are used.
        """

        self.data['password'] = 'wrong'
        self.response = self.client.post(
            'http://127.0.0.1:8000/api/token/', self.data, format='json')
        # print(response)
        self.assertEqual(self.response.status_code, 401)


class UserListTest(BaseTestCase):
    
    def test_unauthorized_cannot_see_page(self):

        response = self.client.get("http://127.0.0.1:8000/users/")
        self.assertEquals(response.status_code, 401)

    def test_authorized_can_see_page(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        self.response = self.client.get(
            "http://127.0.0.1:8000/users/")
        self.assertEqual(self.response.status_code, 200)


class RegisterUserTest(BaseTestCase):
    def setUp(self):
        self.register_data = {
            "username": "tests",
            "password": "test1234",
            "email": "test@test.com",
            "first_name": "testfirstname",
            "last_name": "testlastname",
            "member_position": "Worker"
        }
        return super().setUp()

    def test_unauthorized_cannot_see_page(self):
        response = self.client.get("http://127.0.0.1:8000/users/register")
        self.assertEquals(response.status_code, 401)

    def test_authorized_but_not_admin_can_register(self):
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.post(
            "http://127.0.0.1:8000/users/register", self.register_data, format='json')
        
        self.assertEquals(response.status_code, 403)
    
    def test_admin_can_register(self):
        self.user.is_admin = True
        self.user.is_staff = True
        self.user.save()
        self.response = self.client.post(
            'http://127.0.0.1:8000/api/token/', self.data)
        new_access_token = self.response.data['access']
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {new_access_token}')
        response = self.client.post(
            "http://127.0.0.1:8000/users/register", self.register_data, format='json')
        self.assertEquals(response.status_code, 200)
