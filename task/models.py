from operator import truediv
from django.db import models
from django.contrib.auth.models import User
from appliances.models import Appliance
# Create your models here.

class Task(models.Model):
    TASK_TYPES = (
        ('Inspection', 'Inspection'),
        ('Diagnostic', 'Diagnostic'),
        ('Repair', 'Repair'),
        ('Other', 'Other')
    )
    task_type = models.CharField(max_length=20, choices=TASK_TYPES)
    task_description = models.TextField()
    tast_creation_time = models.DateTimeField(auto_now_add=True)
    task_creator = models.ForeignKey(User, on_delete=models.CASCADE)
    task_appliance = models.ForeignKey(Appliance, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.task_type)
