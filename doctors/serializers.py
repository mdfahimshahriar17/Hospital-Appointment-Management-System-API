from rest_framework import serializers
from .models import Doctor


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = [
            'id',
            'name',
            'department',
            'specialization',
            'visiting_fee',
        ]

    def validation_fee(self, value):
        if value < 0:
            raise serializers.ValidationError(
                "Visiting fee cannot be negative."
            )
        return value