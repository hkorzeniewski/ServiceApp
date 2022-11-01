from rest_framework import permissions

class AddAppliancePermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            print('hello superuser')
            return True
        
        if request.user.has_perm('appliances.add_appliance'):
            print("I got permission")
            return True

        return False


class UpdateAppliancePermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            print('hello superuser')
            return True

        if request.user.has_perm('appliances.change_appliance'):
            print("I got permission")
            return True

        return False
    