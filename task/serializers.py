from asyncore import read
import imp
from urllib import request
from rest_framework import serializers
from .models import Task
from users.serializers import UserSerializer

class TaskSerializer(serializers.ModelSerializer):
    # task_appliance = serializers.SlugRelatedField(
    #     read_only=False, slug_field="name")
    class Meta:
        model = Task
        fields = ('id', 'task_type', 'task_description', 'task_appliance', 'task_worker', 'task_creation_time')


