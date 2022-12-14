from email.mime import base
from rest_framework import routers
from .views import UserListViewSet, RegisterUserViewSet, LoginView, UserView, RegisterUser
from django.urls import path
from . import views

from django.contrib.auth import get_user_model

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

router = routers.SimpleRouter()
router.register('admin', RegisterUserViewSet)
# router.register('', UserListViewSet, basename='users')
# router.register('register', RegisterUser.as_view(), basename='register')
urlpatterns = router.urls

urlpatterns = [
    path('register', RegisterUser.as_view()),
    path('serviceapp/login', views.login_view, name='login'),
    path('user', UserView.as_view()),
    path('logout', views.logout_view, name='logout'),
    path('', UserListViewSet.as_view({'get': 'list'}))
]
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format)
    })