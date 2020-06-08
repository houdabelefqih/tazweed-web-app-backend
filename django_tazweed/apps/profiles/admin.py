from django.contrib import admin
from .models import Client, Seller, User

# Register your models here.
class ClientAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

class SellerAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(User)
admin.site.register(Client, ClientAdmin)
admin.site.register(Seller, SellerAdmin)
