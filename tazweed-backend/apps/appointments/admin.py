from django.contrib import admin
from .models import Slot, Appointment

class SlotAdmin(admin.ModelAdmin):
    readonly_fields = ('uuid','id')

class AppointmentAdmin(admin.ModelAdmin):
    readonly_fields = ('uuid', 'id')

admin.site.register(Slot, SlotAdmin)
admin.site.register(Appointment, AppointmentAdmin)
