from django.db import models
from apps.profiles.models import Client, Seller


class Slot(models.Model):
    date= models.DateField()
    start = models.TimeField()
    end = models.TimeField()
    available = models.BooleanField(default=True)
    seller = models.ForeignKey(Seller, related_name="slots", on_delete=models.CASCADE)



class Appointment(models.Model):
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE, null=True)
    client = models.ForeignKey(Client, related_name="reservations", on_delete=models.CASCADE)
    approved = models.BooleanField(default=True)
    