from os import stat
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Appliance
from .serializers import ApplianceSerializer

# Create your views here.

class ApplianceViewSet(viewsets.ModelViewSet):
    queryset = Appliance.objects.all()
    serializer_class = ApplianceSerializer

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
