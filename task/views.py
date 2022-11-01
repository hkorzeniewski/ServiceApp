from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Task
from .serializers import TaskSerializer
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated

# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes=[IsAuthenticated]


    def perform_create(self, serializer):
        serializer.save(task_creator=self.request.user)
