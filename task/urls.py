from decimal import DefaultContext
from xml.etree.ElementInclude import include
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from django.urls import path
from task import views

from .views import TaskView

router = DefaultRouter()
# router.register(r'serviceapp/tasks', views.TaskViewSet, basename="tasks")

urlpatterns = [
    path("serviceapp/tasks-list/", TaskView.as_view(), name="tasks")
]
urlpatterns += router.urls
