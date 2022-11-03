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


# class AdminCreateUserTest(APITestCase):
#     def setUp(self):
#         self.client = APIClient()
#         # self.client = client.get("http://127.0.0.1:8000/users/admin")
#         self.superuser = User.objects.create_superuser(
#             username='testuser', email='test@test.com', password='test1234' )
#         self.superuser.is_superuser = True
#         self.superuser.is_staff = True
#         self.superuser.save()
#         # self.client.login(username='test', password='testpassword')
#         self.data = { 
#             "username": "tests", 
#             "password": "test1234", 
#             "email": "test@test.com", 
#             "first_name": "testfirstname", 
#             "last_name": "testlastname", 
#             "member_position": "Worker"
#             }

#     def test_admin_can_create_user(self):
#         self.client.force_login(user=self.superuser)
#         # print(self.superuser.is_superuser)

#         response = self.client.post(
#             "http://127.0.0.1:8000/users/admin/", self.data, format='json')
#         # print(response.data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)



class TestCustomResponsePayload(BaseTestCase):

    def test_jwt_login_custom_response_json(self):
        """
        Ensure JWT login view using JSON POST works.
        """
        client = APIClient(enforce_csrf_checks=True)
        # print(self.data)
        response = client.post(
            "http://127.0.0.1:8000/api/token/", self.data, format='json')
        # response = self.client.get("http://127.0.0.1:8000/users/login")
        # print(response.data)
        decoded_payload = utils.jwt_decode_handler(response.data['access'])
        decoded_username = utils.jwt_payload_handler(self.user)
        # print(decoded_username['username'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(decoded_username['username'], self.username)


class ObtainJSONWebTokenTests(BaseTestCase):
    def test_jwt_login_form(self):
        client = APIClient(enforce_csrf_checks=True)

        response = client.post('http://127.0.0.1:8000/api/token/', self.data)
        # print(client)
        # decoded_payload = utils.jwt_decode_handler(response.data['access'])
        decoded_username = utils.jwt_payload_handler(self.user)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(decoded_username['username'], self.username)

    def test_jwt_login_json_bad_creds(self):
        """
        Ensure JWT login view using JSON POST fails
        if bad credentials are used.
        """
        client = APIClient(enforce_csrf_checks=True)

        self.data['password'] = 'wrong'
        response = client.post(
            'http://127.0.0.1:8000/api/token/', self.data, format='json')
        # print(response)
        self.assertEqual(response.status_code, 401)


class UserListTest(BaseTestCase):
    
    def test_unauthorized_cannot_see_page(self):

        response = self.client.get("http://127.0.0.1:8000/users/")
        self.assertEquals(response.status_code, 401)

    def test_authorized_can_see_page(self):
        client = APIClient(enforce_csrf_checks=True)
        response = client.post('http://127.0.0.1:8000/api/token/', self.data)
        print(response.data)
        # self.client.force_login(user=self.user)
        print(response.data['access'])
        response = self.client.get("http://127.0.0.1:8000/users/", headers = {'Authorization': 'Token ' + response.data['access']})
        print(response)
        self.assertEqual(response.status_code, 200)
        self.client.logout()
