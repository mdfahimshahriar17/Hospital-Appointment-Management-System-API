from django.shortcuts import render
from rest_framework import generics

from .models import Billing
from .serializers import BillingSerializer
from .permissions import BillingPermission

class BillingListCreateView(generics.ListCreateAPIView):
    serializer_class = BillingSerializer
    permission_classes = [BillingPermission]


    def get_queryset(self):
        user = self.request.user

        if user.role == 'admin':
            return Billing.objects.all()

        if user.role == 'patient':
            return Billing.objects.filter(patient=user)

        if user.role == 'doctor':
            return Billing.objects.filter(doctor__name=user.full_name)
        
        return Billing.objects.none()


    def perform_create(self, serializer):
        serializer.save(patient=self.request.user)


class BillingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Billing.objects.all()
    serializer_class = BillingSerializer
    permission_classes = [BillingPermission]