from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from accounts.models import User
from doctors.models import Doctor
from appointments.models import Appointment


class DashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = {
            'total_patients': User.objects.filter(
                role='patient'
            ).count(),

            'total_doctors': Doctor.objects.count(),

            'total_appointments': Appointment.objects.count(),

            'pending_appointments': Appointment.objects.filter(
                status='pending'
            ).count(),

            'completed_appointments': Appointment.objects.filter(
                status='completed'
            ).count(),
        }

        return Response(data)