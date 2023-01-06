from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status, permissions,renderers, generics
from rest_framework.decorators import action, permission_classes
from rest_framework.mixins import RetrieveModelMixin, CreateModelMixin, ListModelMixin, UpdateModelMixin
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated, IsAdminUser
from django.contrib.auth.mixins import PermissionRequiredMixin

from .serializers import PartSerializer
from rest_framework.response import Response
from .models import Part, ElectronicPart
# Create your views here.

class PartListViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PartSerializer

    def get_queryset(self):
        queryset = Part.objects.all()
        return queryset

    @action(detail=False, methods=['POST'], permission_classes = [IsAuthenticated])
    def substract(self, request, *args, **kwargs):
        user = request.user
        part = request.data

        parts = Part.objects.filter(id__in=part[""])

        return Response(part)

class PartDetailViewSet(UpdateModelMixin, RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Part.objects.all()
    serializer_class = PartSerializer

    def retrieve(self, request, pk):
        print(request.data)
        part = get_object_or_404(Part, pk=pk)
        serializer = PartSerializer(part)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        part = get_object_or_404(Part, pk=pk) 
        serializer = PartSerializer(part, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return(serializer.errors, status.HTTP_400_BAD_REQUEST)

