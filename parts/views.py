from django.shortcuts import render
from rest_framework import viewsets, status, permissions,renderers, generics

from .serializers import PartSerializer
from .models import Part, ElectronicPart
# Create your views here.

class PartListViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Part.objects.all()
    serializer_class = PartSerializer