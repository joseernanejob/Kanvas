from rest_framework import permissions
from rest_framework.views import View


class isAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
            and request.user.is_superuser
        )
