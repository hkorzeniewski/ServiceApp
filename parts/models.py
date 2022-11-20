from django.db import models
from users.models import User
# Create your models here.

class Part(models.Model):
    PART_TYPES = (
        ('Electronic', 'Electronic'),
        ('Water', 'Water'),
        ('Mechanical', 'Mechanical'),
        ('Other', 'Other')
    )

    name = models.CharField(max_length=100, blank=False)
    serial_number = models.CharField(max_length=20, blank=True, default='')
    quantity = models.IntegerField()
    price = models.FloatField(blank=True)
    part_addition_time = models.DateTimeField(auto_now_add=True)
    part_adder = models.ForeignKey(User, related_name='part_adder', on_delete=models.CASCADE)
    part_type = models.CharField(max_length=20, choices=PART_TYPES)
    part_description = models.TextField()
    to_buy = models.BooleanField()

    def substract_quantity(self, quantity):
        self.quantity -= quantity
        self.save()

    def add_quantity(self, quantity):
        self.quantity += quantity
        self.save()     

    def is_to_buy(self ):
        if self.quantity < 2:
            self.to_buy = True
            self.save()   

    def __str__(self):
        return self.name

class ElectronicPart(Part):
    TECHNOLOGY_TYPES = (
        ('SMT', 'SMT'),
        ('THT', 'THT')
    )

    surface_mount_technology = models.CharField(max_length=20, choices=TECHNOLOGY_TYPES)
    pin_quantity = models.IntegerField()
    resistance = models.CharField(max_length=20, blank=True)
    capacity = models.CharField(max_length=20, blank=True)
    tolerance = models.FloatField(blank=True)