from .serializers import (
    HostpitalSerializer,
    ChildSerializer,
    VaccinationSerializer,
)
from rest_framework import generics, permissions, authentication
from .models import Hospital, Child, Appointment, Vaccinaton


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


# Admin
class GetAdminHospital(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = HostpitalSerializer

    def get_queryset(self):
        return Hospital.objects.filter(admin=self.request.user)
    

class ConfirmDiseaseForHospital(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = VaccinationSerializer

    def get_queryset(self):
        disease = self.request.query_params.get("disease")  # Get 'disease' from query params
        if disease:
            return Vaccinaton.objects.filter(parent=self.request.user, disease=disease)
        return Vaccinaton.objects.none()