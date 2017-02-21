from rest_framework.permissions import BasePermission
from rest_framework.compat import is_authenticated


class UserPermission(BasePermission):

    def has_permission(self, request, view):
        """
        if super user allow him to do anything
        When not super user dont allow him to list
        """
        if view.action == "list":
            return request.user.is_superuser
        return True

    def has_object_permission(self, request, view, obj):
        """
        Allow retrieve, update and delete when content belongs to user
        Allow superusers
        """
        return request.user.is_superuser or request.user == obj

class ProfilePermission(BasePermission):

    def has_permission(self, request, view):
        if view.action == "create":
            return request.user.is_superuser or int(view.kwargs["user_id"]) == request.user.id
        return is_authenticated(request.user)

    def has_object_permission(self, request, view, obj):
        return view.action == "retrieve" or request.user.is_superuser or request.user == obj.user
