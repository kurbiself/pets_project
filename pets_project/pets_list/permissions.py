from rest_framework import permissions

class NotBobPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and 'Bob' not in request.user.username:
            return True
        else:
            return False
    
    def has_object_permission(self, request, view, obj):
        return True
    
