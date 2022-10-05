from email.policy import default
from random import choices
from django.db import models
from django.contrib.auth.models import User

class Appliance(models.Model):

    name = models.CharField(max_length=100, blank=False)
    serial_number = models.CharField(max_length=20, blank=True, default='')
    # appliance_purpose = models.CharField(max_length=20, choices= APPLIANCE_PURPOSE)
    creation_time = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    creator = models.ForeignKey(User, related_name='creator', on_delete=models.CASCADE)