from asyncore import read
import imp
from urllib import request
from rest_framework import serializers
from .models import Task
from users.serializers import UserSerializer

class TaskSerializer(serializers.ModelSerializer):
    task_creator = serializers.SlugRelatedField(
        read_only=True, slug_field="username")
    class Meta:
        model = Task
        fields = ('id', 'task_type', 'task_description', 'task_appliance','task_creator' ,'task_worker', 'task_creation_time')


