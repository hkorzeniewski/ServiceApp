from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from appliances import views


urlpatterns = [
    path('appliances/', views.ApplianceList.as_view()),
    path('appliances/<int:pk>/', views.ApplianceDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)