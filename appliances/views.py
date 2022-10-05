import imp
from os import stat
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Appliance
from .serializers import ApplianceSerializer

# Create your views here.
class ApplianceList(APIView):
    def get(self, request, format=None):
        serializer_context = {
            'request': request,
        }
        appliances = Appliance.objects.all()
        serializer = ApplianceSerializer(appliances, many=True, context=serializer_context)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ApplianceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ApplianceDetail(APIView):
    def get_object(self, pk):
        try:
            return Appliance.objects.get(pk=pk)
        except Appliance.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, pk, format=None):
        appliance = Appliance.objects.get(pk=pk)
        serializer_context = {
            'request': request,
        }
        serializer = ApplianceSerializer(appliance, context=serializer_context)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        appliance = Appliance.objects.get(pk=pk)
        serializer = ApplianceSerializer(appliance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        appliance = Appliance.objects.get(pk=pk)
        appliance.delete()
        return Response(staus=status.HTTP_204_NO_CONTENT)
