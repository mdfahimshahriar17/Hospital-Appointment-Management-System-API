from rest_framework.permissions import BasePermission


class BillingPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        user = request.user

        if user.role == 'admin':
            return True

        if user.role == 'patient':
            return obj.patient == user

        if user.role == 'doctor':
            return obj.doctor.name == user.full_name

        return False