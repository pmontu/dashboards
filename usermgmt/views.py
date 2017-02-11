from django.contrib.auth.models import User
from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import ModelViewSet

from .serializers import UserSerializer

class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def perform_create(self, serializer):
        username = serializer.validated_data["username"]
        try:
            if User.objects.get(username=username):
                raise serializers.ValidationError("User already exists")
        except User.DoesNotExist:
            serializer.save()
