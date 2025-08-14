from rest_framework import permissions

class IsAdminUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.submitted_by == request.user or request.user.role == 'admin'
    
    
    
