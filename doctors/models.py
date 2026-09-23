from django.db import models


class Doctor(models.Model):
    name = models.CharField()
    department = models.CharField()
    specialization = models.CharField()
    visiting_fee = models.DecimalField()
