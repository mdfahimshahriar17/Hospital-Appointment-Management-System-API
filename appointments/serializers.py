from rest_framework import serializers
from django.utils import timezone

from .models import Appointment


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = [
            'id',
            'patient',
            'doctor',
            'appointment_date',
            'appointment_time',
            'status',
        ]
        read_only_fields = ['patient']

    def validate_appointment_data(self, value):
        if value < timezone.localdate():
            raise serializers.ValidationError(
                "Appointment date cannot be in the past"
            )
        return value