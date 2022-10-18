from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient, force_authenticate
from rest_framework import status


from .models import User
from .serializers import UserListSerializer, UserAdminSerializer
# Create your tests here.

class AdminCreateUserTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        # self.client = client.get("http://127.0.0.1:8000/users/admin")
        self.superuser = User.objects.create_superuser(
            username='testuser', email='test@test.com', password='test1234' )
        self.superuser.is_superuser = True
        self.superuser.is_staff = True
        self.superuser.save()
        # self.client.login(username='test', password='testpassword')
        self.data = { 
            "username": "tests", 
            "password": "test1234", 
            "email": "test@test.com", 
            "first_name": "testfirstname", 
            "last_name": "testlastname", 
            "member_position": "Worker"
            }

    def test_admin_can_create_user(self):
        self.client.force_login(user=self.superuser)
        # print(self.superuser.is_superuser)

        response = self.client.post(
            "http://127.0.0.1:8000/users/admin/", self.data, format='json')
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class UserListTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', email='test@test.com', password='1234')

    def test_unauthenticated_can_see_page(self):

        response = self.client.get("http://127.0.0.1:8000/users/")
        self.assertEquals(response.status_code, 403)

    def test_authenticated_can_see_page(self):
        self.client.force_login(user=self.user)
        response = self.client.get("http://127.0.0.1:8000/users/")
        self.assertEqual(response.status_code, 200)
        self.client.logout()
