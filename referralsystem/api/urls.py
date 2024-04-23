from rest_framework.routers import DefaultRouter
from api.views import UserViewSet
from django.urls import include, path


router = DefaultRouter()
router.register('user', UserViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
]
