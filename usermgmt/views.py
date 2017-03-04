from django.contrib.auth.models import User
from rest_framework import viewsets
# from rest_framework import mixins

from utils.mixins import MultiSerializerViewSetMixin
from .serializers import UserSerializer, UserPatchSerializer
from .permissions import AnyoneSignUpOrIsAdminOrIsOwner


class UserViewSet(
		MultiSerializerViewSetMixin,
		viewsets.ModelViewSet):
	serializer_class = UserSerializer
	serializer_action_classes = {
		'update': UserPatchSerializer
	}
	queryset = User.objects.filter()
	permission_classes = (AnyoneSignUpOrIsAdminOrIsOwner, )

	def perform_destroy(self, instance):
		if instance.customer.picture:
			instance.customer.picture.delete()
		super(UserViewSet, self).perform_destroy(instance)