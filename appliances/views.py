from os import stat
from django.shortcuts import render
from rest_framework import viewsets, status, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.mixins import RetrieveModelMixin, CreateModelMixin, ListModelMixin
from rest_framework.permissions import DjangoModelPermissions
from django.contrib.auth.mixins import PermissionRequiredMixin


from .models import Appliance
from .serializers import ApplianceSerializer
from users.models import User

# Create your views here.

class ApplianceViewSet(ListModelMixin, viewsets.GenericViewSet):
    queryset = Appliance.objects.all()
    serializer_class = ApplianceSerializer
    permission_classes =[permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

class ApplianceWorkerViewSet(PermissionRequiredMixin, CreateModelMixin, RetrieveModelMixin, ListModelMixin, viewsets.GenericViewSet):
    queryset = Appliance.objects.all()
    serializer_class = ApplianceSerializer
    permission_classes = [DjangoModelPermissions]