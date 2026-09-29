from rest_framework import serializers
from billing.models import Billing
from doctors.models import Doctor



class BillingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Billing
        fields = [
            'id',
            'patient', 
            'doctor', 
            'appointment', 
            'consultation_fee', 
            'discount', 
            'total_amount']

        read_only_fields = ['patient', 'consultation_fee', 'total_amount']

    def validate(self, attrs):
        if attrs['discount'] < 0:
            raise serializers.ValidationError("Discount amount must be  greaterthan 0.")
        elif attrs['discount'] > attrs['appointment'].doctor.visiting_fee:
            raise serializers.ValidationError("Dicount amoun must be lessthan consaltation fee.")

        return attrs

    def create(self, validated_data):
        appointment = validated_data['appointment']
        doctor = appointment.doctor
        consultation_fee = doctor.visiting_fee
        total_amount = consultation_fee - validated_data['discount']

        validated_data['doctor'] = doctor
        validated_data['consultation_fee'] = consultation_fee
        validated_data['total_amount'] = total_amount

        bill = Billing.objects.create(**validated_data)
        return bill