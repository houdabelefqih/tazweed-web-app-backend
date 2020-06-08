from django.contrib import admin
from .models import Slot, Appointment

class SlotAdmin(admin.ModelAdmin):
    readonly_fields = ('uuid',)

class AppointmentAdmin(admin.ModelAdmin):
    readonly_fields = ('uuid',)

admin.site.register(Slot, SlotAdmin)
admin.site.register(Appointment, AppointmentAdmin)
