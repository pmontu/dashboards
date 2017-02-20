from django.contrib.auth.models import User
from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import ModelViewSet
from rest_framework import serializers

from .serializers import UserSerializer, UserDetailSerializer
from .permissions import UserPermission
from utils.mixins import MultiSerializerViewSetMixin


class UserViewSet(MultiSerializerViewSetMixin, ModelViewSet):
    serializer_class = UserSerializer
    serializer_action_classes = {
        'update': UserDetailSerializer,
    }
    permission_classes = (UserPermission,)
    queryset = User.objects.all()

    def perform_create(self, serializer):
        username = serializer.validated_data["username"]
        try:
            if User.objects.get(username=username):
                raise serializers.ValidationError("User already exists")
        except User.DoesNotExist:
            serializer.save()

    def get_object(self):
        pk = self.kwargs.get('pk')
        if pk == "current":
            return self.request.user
        return super(UserViewSet, self).get_object()

