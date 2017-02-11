from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializerMixin(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=30)
    first_name = serializers.CharField(max_length=30, required=False, allow_blank=True)
    last_name = serializers.CharField(max_length=30, required=False, allow_blank=True)
    email = serializers.EmailField(required=False, allow_blank=True)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        password = validated_data.get('password', '')
        if password:
            instance.set_password(password)
            instance.save()
        return instance

    class Meta:
        model = User


class UserSerializer(UserSerializerMixin):
    password = serializers.CharField(
        max_length=128, write_only=True,
        style={'input_type': 'password'})


class UserDetailSerializer(UserSerializerMixin):
    password = serializers.CharField(
        max_length=128, write_only=True,
        style={'input_type': 'password'},
        required=False, allow_blank=True
    )
