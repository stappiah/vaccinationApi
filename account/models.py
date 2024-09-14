# In your app's models.py file
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from base.models import Hospital

USER_TYPES = [
    ("admin", "Administrator"),
    ("mother", "Mother"),
    ("nurse", "Nurse"),
    ("doctor", "Doctor"),
    ("receptionist", "Receptionist"),
    ("other", "Other"),
]

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


class AccountManager(BaseUserManager):
    def create_user(self, email, user_type, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email).lower()
        user = self.model(email=email, user_type=user_type, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, "admin", password, **extra_fields)


class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user_type = models.CharField(max_length=13, choices=USER_TYPES)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=64, blank=True, null=True)
    region = models.CharField(
        choices=LOCATION_REGION, max_length=20, blank=True, null=True
    )
    hospital = models.ForeignKey(
        Hospital,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="hospital_users",
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    profile_image = models.ImageField(upload_to="user_images/", null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    objects = AccountManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email
