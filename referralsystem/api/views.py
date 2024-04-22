from rest_framework import viewsets
from rest_framework.viewsets import GenericViewSet
from api.serializers import UserSerializer
from rest_framework import mixins

from users.models import User, InvitedUsers


class UserViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    # http_method_names = ['get', 'post']
    queryset = User.objects.all()
    serializer_class = UserSerializer
