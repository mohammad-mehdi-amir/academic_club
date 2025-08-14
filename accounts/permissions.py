
from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role == 'admin'

class IsMemberOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role in ('member', 'admin')

class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return getattr(request.user, 'is_authenticated', False) and (obj == getattr(request.user, 'profile', None) or getattr(obj, 'submitted_by', None) == request.user or getattr(obj, 'created_by', None) == request.user or request.user.role == 'admin')