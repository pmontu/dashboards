from rest_framework import permissions
from rest_framework.compat import is_authenticated


class AnyoneSignUpOrIsAdminOrIsOwner(permissions.BasePermission):
	"""
	Alow all to signup.
	Allow admin to view other users.
	Allow owners and admin to patch, retrieve and destroy.
	"""
	
	def has_permission(self, request, view):
		if view.action == "create":
			return True
		elif view.action in ["update", "retrieve", "destroy"] \
			and is_authenticated(request.user):
			return True
		elif view.action == "list" and request.user.is_superuser:
			return True
		return False

	def has_object_permission(self, request, view, obj):
		if view.action in ["update", "retrieve", "destroy"] \
			and (obj == request.user or request.user.is_superuser):
			return True
		return False
