from .serializers import (
    HostpitalSerializer,
    ChildSerializer,
    VaccinationSerializer,
    AppointmentSerializer,
)
from rest_framework import generics, permissions, authentication
from .models import Hospital, Child, Appointment, Vaccinaton
from django.db.models import Q
from account.serializers import AccountPropertiesSerializer
from account.models import Account


# Create your views here.
class CreateListHostpital(generics.ListCreateAPIView):
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


class RetrieveUpdateDeleteChild(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = ChildSerializer
    queryset = Child.objects.all()


class RetrieveParentChild(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = ChildSerializer

    def get_queryset(self):
        parent_id = self.request.user.id
        return Child.objects.filter(parent=parent_id)


class ListParentChild(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = ChildSerializer

    def get_queryset(self):
        parent_id = self.kwargs.get("pk")
        return Child.objects.filter(parent=parent_id)


class CreateVaccination(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = VaccinationSerializer
    queryset = Vaccinaton.objects.all()


class RetrieveUpdateVaccination(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = VaccinationSerializer
    queryset = Vaccinaton.objects.all()


# Admin
class GetAdminHospital(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = HostpitalSerializer

    def get_queryset(self):
        if hasattr(self.request.user, "hospital") and self.request.user.hospital:
            hospital_id = self.request.user.hospital.id
            queryset = Hospital.objects.filter(
                Q(admin=self.request.user) | Q(id=hospital_id)
            )
            return queryset
        return Hospital.objects.filter(admin=self.request.user)


class GetHospitalVaccination(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = VaccinationSerializer

    def get_queryset(self):
        hospital_id = self.kwargs.get("pk")
        queryset = Vaccinaton.objects.filter(hospital=hospital_id)
        return queryset


class ConfirmDiseaseForHospital(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = VaccinationSerializer

    def get_queryset(self):
        disease = self.request.query_params.get(
            "disease"
        )  # Get 'disease' from query params
        if disease:
            return Vaccinaton.objects.filter(parent=self.request.user, disease=disease)
        return Vaccinaton.objects.none()


class CreateAppointment(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()


class UpdateAppointment(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()


class RetrieveParentAppointment(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        return Appointment.objects.filter(parent=self.request.user)


class RetrieveHospitalAppointment(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        hospital_id = self.kwargs.get("pk")
        return Appointment.objects.filter(hospital=hospital_id)


class GetHospitalMothers(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = AccountPropertiesSerializer

    def get_queryset(self):
        hospital_id = self.request.query_params.get("hospital")
        # hospital_id = self.request.query_params.get('hospital')
        parents = (
            Vaccinaton.objects.filter(hospital=hospital_id)
            .values_list("parent", flat=True)
            .distinct()
        ).order_by("-date_taken")
        parent_users = Account.objects.filter(id__in=parents)
        return parent_users


class GetHospitalUsers(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = AccountPropertiesSerializer

    def get_queryset(self):
        hospital_id = self.request.query_params.get("hospital")
        # hospital_id = self.request.query_params.get('hospital')
        parents = (
            Vaccinaton.objects.filter(hospital=hospital_id)
            .values_list("parent", flat=True)
            .distinct()
        )
        parent_users = Account.objects.filter(
            Q(id__in=parents) | Q(hospital=hospital_id)
        ).order_by("-date_joined")
        return parent_users
