from decimal import DefaultContext
from xml.etree.ElementInclude import include
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from django.urls import path
from task import views

router = DefaultRouter()
router.register(r'tasks', views.TaskViewSet, basename="tasks")

urlpatterns = router.urls