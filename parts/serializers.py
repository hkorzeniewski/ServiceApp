from rest_framework import serializers
from .models import Part, ElectronicPart

class PartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = (
            "name",
            "serial_number",
            "quantity",
            "price",
            "part_addition_time",
            "part_adder",
            "part_type",
            "part_description",
            "to_buy"

        )