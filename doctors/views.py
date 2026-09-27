from django.shortcuts import render

from rest_framework import generics
from .models import Doctor
from .serializers import DoctorSerializer
from .permissions import IsAdminOrReadOnly

class DoctorListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    filterset_fields = ['department']


class DoctorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAdminOrReadOnly]