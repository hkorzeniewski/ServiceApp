from datetime import datetime
from urllib import response
import jwt, datetime
from multiprocessing import AuthenticationError
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import UserAdminSerializer, UserSerializer
from .models import User

# Create your views here.
class UserAdminViewSet(viewsets.ModelViewSet):


    queryset = User.objects.all()
    serializer_class = UserAdminSerializer
    permission_classes = [DjangoModelPermissions]

    def get_object(self):
        pk = self.kwargs.get('pk')

        if pk == "current":
            return self.request.user
            
        return super().get_object()


class UserListViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes =[DjangoModelPermissions]


class RegisterUser(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class LoginView(APIView):

    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        user = User.objects.filter(username=username).first()

        if user is None:
            raise AuthenticationError('User not found')

        if not user.check_password(password):
            raise AuthenticationError('Wrong password')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }
        token = jwt.encode(payload, 'key', algorithm='HS256')
        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }

        return response