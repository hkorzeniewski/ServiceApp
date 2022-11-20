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
    # queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes=[IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['task_type', 'task_worker__username']

    def perform_create(self, serializer):
        serializer.save(task_creator=self.request.user)
    
    def get_queryset(self):
        queryset = Task.objects.all()
        username = self.request.query_params.get('task_worker')
        # print(self.request.query_params)
        # print(username)
        # print(queryset.filter(task_worker__username='hkorz'))
        if username is not None:
            queryset = queryset.filter(task_worker__username=username)
        return queryset


