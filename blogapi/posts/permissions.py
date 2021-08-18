from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # only see
        if request.method in permissions.SAFE_METHODS:
            return True
        # is_write
            return obj.author == request.user