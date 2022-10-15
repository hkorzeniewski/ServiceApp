from rest_framework import routers
from .views import UserListViewSet

from users.views import UserAdminViewSet
from django.contrib.auth import get_user_model

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

router = routers.SimpleRouter()
router.register('admin', UserAdminViewSet)
router.register('', UserListViewSet, basename='users')
urlpatterns = router.urls

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format)
    })