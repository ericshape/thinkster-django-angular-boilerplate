# created by Ji Wang ericshape @ 2/13/16 12:08 AM

from rest_framework import permissions


class IsAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, account):
        if request.user:
            return account == request.user
        return False