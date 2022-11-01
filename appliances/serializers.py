from email.policy import default
from urllib import request
from rest_framework import serializers
import urllib.request


from users.serializers import UserSerializer
from .models import Appliance
from task.serializers import TaskSerializer
from django.contrib.auth.models import User


class ApplianceSerializer(serializers.HyperlinkedModelSerializer):

    creator = serializers.SlugRelatedField(
        read_only=True, slug_field="username")
    tasks = TaskSerializer(read_only=True, many=True)
    class Meta:
        model = Appliance
        fields = (
            "id",
            "name",
            "serial_number",
            "creation_time",
            "description",
            "creator",
            "tasks",
        )
    
