from django.contrib import admin
from .models import Hospital, Child, Vaccinaton, Appointment, Availability

# Register your models here.
admin.site.register(Hospital)
admin.site.register(Child)
admin.site.register(Vaccinaton)
admin.site.register(Appointment)
admin.site.register(Availability)