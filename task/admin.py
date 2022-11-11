from django.contrib import admin

from .models import Task
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_type', 'task_description', 'task_creation_time', 'task_creator', 'task_appliance', 'task_worker')

admin.site.register(Task, TaskAdmin )