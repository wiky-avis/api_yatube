from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ('DELETE', 'PUT', 'PATCH', 'POST'):
            return request.user == obj.author
        return True
