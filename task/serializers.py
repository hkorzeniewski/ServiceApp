import imp
from rest_framework import serializers
from .models import Task
from users.serializers import UserSerializer

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'task_type', 'task_description', 'task_creation_time')