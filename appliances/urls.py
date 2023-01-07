from decimal import DefaultContext
from xml.etree.ElementInclude import include
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from django.urls import path
from appliances import views

from .views import ApplianceView

router = DefaultRouter()
router.register(r'api/appliance/add', views.AddApplianceViewSet, basename="add-appliance")
router.register(r'api/appliance/update', views.UpdateApplianceViewSet, basename="update-appliance")
router.register(r'api/appliances', views.ApplianceViewSet, basename="appliances")
# router.register(r'appliance-list', views.ApplianceView, basename="appliance-list")

urlpatterns = [
    path("serviceapp/appliances-list/", ApplianceView.as_view(), name="appliance-list"),
    path("serviceapp/appliance-add", views.add_appliance, name="add-appliance"),
    path("serviceapp/appliance/<appliance_id>", views.appliance_detail, name='appliance-detail')
]

urlpatterns += router.urls