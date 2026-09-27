from rest_framework.permissions import BasePermission


class AppointmentPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated


    def has_object_permission(self, request, view, obj):
        user = request.user

        if user.role == 'admin':
            return True

        if user.role == 'patient':
            return obj.patient == user and request.method in [
                'GET',
                'HEAD',
                'OPTIONS',
            ]

        if user.role == 'doctor':
            return obj.doctor.name == user.full_name and request.method in [
                'GET',
                'HEAD',
                'OPTIONS',
            ]

        return False