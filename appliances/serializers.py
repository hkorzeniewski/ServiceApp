from rest_framework import serializers

from users.serializers import UserSerializer
from .models import Appliance
from django.contrib.auth.models import User

class ApplianceSerializer(serializers.ModelSerializer):
    creator = UserSerializer(many=False)
    creator = serializers.SlugRelatedField(read_only=True, slug_field="username")
    class Meta:
        model = Appliance
        fields = (
            "id",
            "name",
            "serial_number",
            "creation_time",
            "creator"
        )