from django.db import models

class Vehicle(models.Model):
    plate_number = models.CharField(max_length=20)
    model = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
