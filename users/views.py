import imp
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions

from .serializers import UserAdminSerializer, UserListSerializer
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
    serializer_class = UserListSerializer
    permission_classes =[DjangoModelPermissions]