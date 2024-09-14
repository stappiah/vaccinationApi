from django.db import models
from django.conf import settings

# Create your models here.


LOCATION_REGION = [
    ("Upper West Region", "Upper West Region"),
    ("Upper East Region", "Upper East Region"),
    ("North East Region", "North East Region"),
    ("Northern Region", "Northern Region"),
    ("Savannah Region", "Savannah Region"),
    ("Bono East Region", "Bono East Region"),
    ("Brong Ahafo Region", "Brong Ahafo Region"),
    ("Oti Region", "Oti Region"),
    ("Volta Region", "Volta Region"),
    ("Eastern Region", "Eastern Region"),
    ("Ashanti Region", "Ashanti Region"),
    ("Ahafo Region", "Ahafo Region"),
    ("Western North Region", "Western North Region"),
    ("Western Region", "Western Region"),
    ("Central Region", "Central Region"),
    ("Greater Accra Region", "Greater Accra Region"),
]

DISEASES = [
    ("polio", "polio"),
    ("tetanus", "tetanus"),
    ("pertussis", "pertussis"),
    ("diphtheria", "diphtheria"),
    ("measles", "measles"),
    ("tuberculosis", "tuberculosis"),
]

APPOINTMENT_STATUS = [
    ("cancelled", "Cancelled"),
    ("confirmed", "Confirmed"),
    ("pending", "Pending"),
    ("rescheduled", "Rescheduled"),
]
GENDER = [("male", "Male"), ("female", "Female")]


class Hospital(models.Model):
    admin = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="administered_hospitals",
    )
    name = models.CharField(max_length=60)
    bio = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    region = models.CharField(max_length=20, choices=LOCATION_REGION)
    image = models.ImageField(upload_to="hospital_image")
    start_time = models.TimeField()
    end_time = models.TimeField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Child(models.Model):
    parent = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=6, choices=GENDER)
    date_of_birth = models.DateField()
    date_created = models.DateTimeField(auto_now_add=True)


class Appointment(models.Model):
    parent = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    disease = models.CharField(max_length=12, choices=DISEASES)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    status = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Appointment between {self.parent.first_name} {self.parent.last_name} and {self.hospital.name}"


class Vaccinaton(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.PROTECT)
    parent = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    disease = models.CharField(max_length=12, choices=DISEASES)
    first_dose = models.BooleanField(default=False)
    second_dose = models.BooleanField(default=False)
    third_dose = models.BooleanField(default=False)
    date_taken = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
