from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('doctor', 'Doctor'),
        ('patient', 'Patient'),
    )

    full_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, unique=True)
    address = models.TextField(blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='patient')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []