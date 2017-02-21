from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from rest_framework import serializers

from .serializers import UserSerializer, UserDetailSerializer, ProfileSerializer
from .permissions import UserPermission, ProfilePermission
from .models import Profile
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


class ProfileViewSet(ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = (ProfilePermission,)

    def get_queryset(self):
        user_id = self.kwargs.get("user_id")
        return Profile.objects.filter(user__id=user_id)

    def create(self, request, *args, **kwargs):
        user = User.objects.get(id=kwargs["user_id"])

        if hasattr(user, 'profile'):
            raise serializers.ValidationError("Profile already exists")

        self.kwargs["user"] = user

        return super(ProfileViewSet, self).create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.validated_data["user"] = self.kwargs["user"]
        serializer.save()
