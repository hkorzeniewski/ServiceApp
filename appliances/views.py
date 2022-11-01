import imp
from os import stat
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status, permissions,renderers, generics
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.mixins import RetrieveModelMixin, CreateModelMixin, ListModelMixin, UpdateModelMixin
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated
from django.contrib.auth.mixins import PermissionRequiredMixin


from .models import Appliance
from .serializers import ApplianceSerializer
from .permissions import AddAppliancePermissions, UpdateAppliancePermissions

from users.models import User




# Create your views here.

class ApplianceViewSet(viewsets.ReadOnlyModelViewSet, PermissionRequiredMixin):
    queryset = Appliance.objects.all()
    serializer_class = ApplianceSerializer
    permission_classes =[IsAuthenticated]


    # def perform_create(self, serializer):
    #     serializer.save(creator=self.request.user)

class AddApplianceViewSet(CreateModelMixin, ListModelMixin, viewsets.GenericViewSet):
    queryset = Appliance.objects.all()
    serializer_class = ApplianceSerializer
    # permission_required = ("appliances.add_appliance", "appliances.view_appliance")

    def list(self, request):
        appliances = Appliance.objects.all()
        serializer = ApplianceSerializer(appliances, many=True)
        self.check_object_permissions(request, self.request.user)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = ApplianceSerializer(data=request.data)
        self.check_object_permissions(request, self.request.user)
        if serializer.is_valid(raise_exception=True):
            pass
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    def get_permissions(self):
        if self.action == "list":
            permission_classes = [
                IsAuthenticated,
            ]
        elif self.action == "create":
            permission_classes = [AddAppliancePermissions]
        else: 
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

class UpdateApplianceViewSet(UpdateModelMixin, RetrieveModelMixin, ListModelMixin, viewsets.GenericViewSet):
    queryset = Appliance.objects.all()
    serializer_class = ApplianceSerializer

    def retrieve(self, request, pk):
        appliance = get_object_or_404(Appliance, pk=pk)
        serializer = ApplianceSerializer(appliance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        appliance = get_object_or_404(Appliance, pk=pk) 
        serializer = ApplianceSerializer(appliance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def get_permissions(self):
        if self.action == "list":
            permission_classes = [
                IsAuthenticated,
            ]
        elif self.action == "update":
            permission_classes = [UpdateAppliancePermissions]
        else: 
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    



