from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):

    def has_permission(self, request, view):
        """
        if super user allow him to do anything
        When not super user dont allow him to list
        Allow create, retrieve, update, delete for anonymous
        """
        return view.action != "list" or request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        """
        Allow retrieve, update and delete when content belongs to user
        Allow superusers
        """
        return request.user.is_superuser or request.user == obj
