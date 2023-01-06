from django.contrib import admin
from .models import Part, ElectronicPart
# Register your models here.

class PartsAdmin(admin.ModelAdmin):
    list_display = ('name', 'serial_number', 'quantity')

admin.site.register(Part, PartsAdmin)
admin.site.register(ElectronicPart)