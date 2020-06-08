import uuid
from django.db import models
from apps.profiles.models import Client, Seller
from datetime import datetime


class Slot(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, null=True)   
    date = models.DateField()
    start = models.TimeField()
    end = models.TimeField()
    available = models.BooleanField(default=True)
    seller = models.ForeignKey(Seller, related_name="slots", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.date) + '_'+ str(self.start) + '_' +str(self.seller)
        

class Appointment(models.Model):
    STATUS_CHOICES = [
        ("approved", "approved"),
        ("denied", "denied"),
        ("pending", "pending"),
    ]
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, null=True)
    slot = models.OneToOneField(Slot, on_delete=models.CASCADE, null=True)
    seller = models.ForeignKey(Seller, related_name="appointments", on_delete=models.CASCADE)
    client = models.ForeignKey(Client, related_name="reservations", on_delete=models.CASCADE)
    status = models.CharField(max_length=30,choices=STATUS_CHOICES, default="pending")

    def __str__(self):
        return str(self.slot) + '_'+ str(self.client)