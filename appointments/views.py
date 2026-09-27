from django.shortcuts import render

from rest_framework import generics

from .models import Appointment
from .serializers import AppointmentSerializer
from .permissions import AppointmentPermission


class AppointmentListCreateView(generics.ListCreateAPIView):

    serializer_class = AppointmentSerializer
    permission_classes = [AppointmentPermission]

    def get_queryset(self):
        user = self.request.user

        if user.role == 'admin':
            return Appointment.objects.all()

        if user.role == 'doctor':
            return Appointment.objects.filter(doctor__name=user.full_name)

        if user.role == 'patient':
            return Appointment.objects.filter(patient=user)

        return Appointment.objects.none()

    def perform_create(self, serializer):
        serializer.save(patient=self.request.user)




class AppointmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [AppointmentPermission]
    