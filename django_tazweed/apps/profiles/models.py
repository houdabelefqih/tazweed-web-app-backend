from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_seller = models.BooleanField(default=True)
    phone = models.CharField(max_length=30, blank=True)

class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='client_profile')
	

class Seller(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='seller_profile')
	shop = models.CharField(max_length=30, blank=True)

	def __str__(self):
		return str(self.user)



# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
# 	print('****', created)
# 	if instance.is_seller:
# 		Seller.objects.get_or_create(user = instance)
# 	else:
# 		Client.objects.get_or_create(user = instance)
	
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
# 	print('_-----')	
# 	if instance.is_seller:
# 		instance.seller.save()
# 	else:
# 		instance.client.save()


