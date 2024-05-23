from rest_framework import serializers
from .models import Hospital, Child, Appointment, Vaccinaton, Availability


class HostpitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = "__all__"


class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = "__all__"


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = "__all__"


class VaccinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaccinaton
        fields = "__all__"


class AvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Availability
        fields = "__all__"
