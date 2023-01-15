from django import forms
from django.forms import ModelForm
from .models import Appliance, AppliancePhoto

from datetime import datetime

class ApplianceForm(ModelForm):
    # creation_time = datetime.now()
    class Meta:
        model = Appliance
        fields = ['name', 'serial_number', 'description']

class AppliancePhotoForm(ModelForm):

    # def __init__(self, *args, **kwargs):
    #     self.appliance_id = kwargs.pop('appliance_id')
    #     super(AppliancePhotoForm,self).__init__(*args, **kwargs)

    class Meta:
        model = AppliancePhoto
        fields = ['image']