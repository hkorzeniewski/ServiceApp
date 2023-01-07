from datetime import datetime
from urllib import response
import jwt, datetime
from rest_framework.exceptions import AuthenticationFailed
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, get_user_model
from rest_framework import viewsets, mixins
from rest_framework.permissions import DjangoModelPermissions, IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth import authenticate

from .serializers import RegisterUserSerializer, UserSerializer
from .models import User
from .forms import LoginForm

# Create your views here.
class RegisterUserViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):


    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer
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
    permission_classes = [IsAdminUser]

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
        user = authenticate(username=username, password=password)
        if user is None:
            raise AuthenticationFailed('User not found')

        if not user.check_password(password):
            raise AuthenticationFailed('Wrong password')

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

class UserView(APIView):

    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated')

        try:
            payload = jwt.decode(token, 'key', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')
        
        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)

class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response


def login_view(request):
    form = LoginForm(request.POST or None)
    print(form)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        # user = authenticate(username=username, password=password)
        user = User.objects.filter(username=username, password=password).first()
        if user is not None:
            login(request, user)
            return redirect("/serviceapp/")
        else:
            print('invalid user')
            request.session['invalid_user'] = 1  # 1 == True
    return render(request, "users/login.html", {"form": form})

def logout_view(request):
    logout(request)
    # request.user == Anon User
    return redirect("/serviceapp/")