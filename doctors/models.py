from django.db import models


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    visiting_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
