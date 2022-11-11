from django.contrib import admin

from .models import Appliance, AppliancePhoto
from task.models import Task

from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html

# Register your models here.

class TaskInline(admin.TabularInline):
    model = Task

class AppliancePhotoInline(admin.StackedInline):
    model = AppliancePhoto
    list_display = ('image_tag', )
    readonly_fields = ('image_tag', )

class ApplianceAdmin(admin.ModelAdmin):
    list_display = ('name', 'serial_number', 'creation_time', 'description', 'creator')
    inlines = [TaskInline, AppliancePhotoInline]


class AppliancePhotoAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'appliance', 'image_added_time')
    readonly_fields = ('image_tag', )

admin.site.register(Appliance, ApplianceAdmin)
admin.site.register(AppliancePhoto, AppliancePhotoAdmin)