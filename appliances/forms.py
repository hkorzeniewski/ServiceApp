from django import forms
from django.forms import ModelForm
from .models import Appliance

from datetime import datetime

class ApplianceForm(ModelForm):
    # creation_time = datetime.now()
    class Meta:
        model = Appliance
        fields = ['name', 'serial_number', 'description', 'creator']