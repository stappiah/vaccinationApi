from .serializers import (
    HostpitalSerializer,
    ChildSerializer,
    AppointmentSerializer,
    VaccinationSerializer,
    AvailabilitySerializer,
)
from rest_framework import generics, permissions, authentication
from .models import Hospital, Child, Appointment, Vaccinaton, Availability


# Create your views here.
class CreateHostpital(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = HostpitalSerializer
    queryset = Hospital.objects.all()


class RetrieveUpdateHostpital(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = HostpitalSerializer
    queryset = Hospital.objects.all()


class CreateChild(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = ChildSerializer
    queryset = Child.objects.all()


class CreateAppointment(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()


class RetrieveUpdateDeleteAppointment(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()


class CreateVaccination(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = VaccinationSerializer
    queryset = Vaccinaton.objects.all()


class RetrieveUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = VaccinationSerializer
    queryset = Vaccinaton.objects.all()


class CreateAvailability(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = AvailabilitySerializer
    queryset = Availability.objects.all()
