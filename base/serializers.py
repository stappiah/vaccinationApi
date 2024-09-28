from rest_framework import serializers
from .models import Hospital, Child, Appointment, Vaccinaton
from django.contrib.auth import get_user_model

Account = get_user_model()


class HostpitalSerializer(serializers.ModelSerializer):
    admin = serializers.PrimaryKeyRelatedField(
        queryset=Account.objects.all(), default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Hospital
        fields = "__all__"


class ChildSerializer(serializers.ModelSerializer):
    parent = serializers.PrimaryKeyRelatedField(
        queryset=Account.objects.all(), default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Child
        fields = "__all__"


class VaccinationSerializer(serializers.ModelSerializer):
    parent = serializers.PrimaryKeyRelatedField(
        queryset=Account.objects.all(), default=serializers.CurrentUserDefault()
    )
    get_parent = serializers.ReadOnlyField()
    get_phone_number = serializers.ReadOnlyField()

    class Meta:
        model = Vaccinaton
        fields = "__all__"


class AppointmentSerializer(serializers.ModelSerializer):
    parent = serializers.PrimaryKeyRelatedField(
        queryset=Account.objects.all(), default=serializers.CurrentUserDefault()
    )
    hospital_name = serializers.ReadOnlyField()
    get_parent = serializers.ReadOnlyField()
    get_phone_number = serializers.ReadOnlyField()

    class Meta:
        model = Appointment
        fields = "__all__"
