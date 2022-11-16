from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend


from .models import Task
from .serializers import TaskSerializer
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated

# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes=[IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['task_type']

    def perform_create(self, serializer):
        serializer.save(task_creator=self.request.user)
    
    # def get_queryset(self):
    #     queryset = Task.objects.all()
    #     print(self.request.user.id)
    #     username = self.request.user.id
    #     if username is not None:
    #         queryset = queryset.filter(task_creator=username)
    #     return queryset


