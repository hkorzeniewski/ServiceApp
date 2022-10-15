from decimal import DefaultContext
from xml.etree.ElementInclude import include
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from django.urls import path
from appliances import views

router = DefaultRouter()
router.register(r'', views.ApplianceViewSet, basename="appliances")

urlpatterns = router.urls