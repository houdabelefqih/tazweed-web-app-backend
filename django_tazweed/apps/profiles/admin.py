from django.contrib import admin
from .models import Client, Seller, User

# Register your models here.
admin.site.register(User)
admin.site.register(Client)
admin.site.register(Seller)
