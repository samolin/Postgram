from rest_framework import SAFE_METHODS, BasePermission


class UserPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_anonymous:
            return request.method in SAFE_METHODS

        if view.basename in ['post']:
            return bool(request.user and request.user.is_authenticated)
        return False

    def has_permission(self, request, view):
        if view.basename in ['post']:
            if request.user.is_anonymous:
                return request.method in SAFE_METHODS
            return bool(request.user and request.user.is_authenticated)

        return False
