from email.policy import default
from urllib import request
from rest_framework import serializers
import urllib.request


from users.serializers import UserSerializer
from .models import Appliance
from task.serializers import TaskSerializer
# from django.contrib.auth.models import User
from users.models import User

class ApplianceSerializer(serializers.ModelSerializer):

    # creator = serializers.SlugRelatedField(
    #     read_only=False, slug_field="username")
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
    
    def create(self, validated_data):
        print(validated_data)
        creator_data = validated_data.pop('creator')
        creator = User.objects.get(username=creator_data)
        print(creator)
        appliance = Appliance.objects.create(name=validated_data["name"], serial_number=validated_data["serial_number"], creation_time=validated_data["creation_time"],
        description=validated_data["description"], creator=creator)
        
        appliance.save()
        return appliance