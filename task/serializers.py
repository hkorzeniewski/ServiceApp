from asyncore import read
import imp
from urllib import request
from rest_framework import serializers
from .models import Task
from users.serializers import UserSerializer

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('id', 'task_type', 'task_description', 'task_appliance', 'task_creation_time')

        # def create(self, validated_data):
        #     request = self.context['request']

        #     appliance_pk = request.data.get('appliance')
        #     validated_data['appliance_id'] = appliance_pk

        #     instance = super().create(validated_data)
        #     return instance
