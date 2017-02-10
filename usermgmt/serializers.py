from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=30)
    password = serializers.CharField(max_length=128)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        # import ipdb; ipdb.set_trace()
        return User.objects.create_user(**validated_data)

    class Meta:
        model = User
        fields = ("id", "username", "password", 'email', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}