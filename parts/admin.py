from django.contrib import admin
from .models import Part, ElectronicPart
# Register your models here.

admin.site.register(Part)
admin.site.register(ElectronicPart)