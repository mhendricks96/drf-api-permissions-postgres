from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
  
  def has_object_permission(self,request, view, obj):

    if request.method in permissions.SAFE_METHODS:
      return True

    if obj.admitted_by is None:
      return True

    return obj.admitted_by == request.user