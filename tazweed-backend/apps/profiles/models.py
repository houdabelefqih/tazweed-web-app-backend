import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_seller = models.BooleanField(default=False)
    phone = models.CharField(max_length=30, blank=True)

	

class Client(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='client')

	class Meta:
		ordering = ["user__last_name","user__first_name"]

	def __str__(self):
		return str(self.user)

	

class Seller(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='seller')
	shop = models.CharField(max_length=30, blank=True)

	class Meta:
		ordering = ["user__last_name","user__first_name"]

	def __str__(self):
		return str(self.user)
