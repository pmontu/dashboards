from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Profile


class UserSerializerMixin(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    is_superuser = serializers.BooleanField(read_only=True)
    first_name = serializers.CharField(max_length=30, required=False, allow_blank=True)
    last_name = serializers.CharField(max_length=30, required=False, allow_blank=True)
    email = serializers.EmailField(required=False, allow_blank=True)
    profile = serializers.SlugRelatedField(
        read_only=True,
        slug_field='id'
     )

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
    username = serializers.CharField(max_length=30)
    password = serializers.CharField(
        max_length=128, write_only=True,
        style={'input_type': 'password'})


class UserDetailSerializer(UserSerializerMixin):
    username = serializers.CharField(read_only=True)
    password = serializers.CharField(
        max_length=128, write_only=True,
        style={'input_type': 'password'},
        required=False, allow_blank=True
    )


class ProfileSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    picture = serializers.ImageField(use_url=False)
    user = serializers.PrimaryKeyRelatedField(
        read_only=True
    )

    def create(self, validated_data):
        return Profile.objects.create(**validated_data)

    class Meta:
        model = Profile
