# In your app's serializers.py
from rest_framework import serializers
from .models import Account
from rest_framework.authtoken.models import Token


class AccountSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = Account
        fields = (
            "email",
            "first_name",
            "last_name",
            "user_type",
            "password",
            "password2",
        )
        extra_kwargs = {
            "password": {"write_only": True},
            "password2": {"write_only": True},  # Add this line
        }

    def create(self, validated_data):
        password = validated_data.get("password")
        password2 = validated_data.get("password2")

        if password != password2:
            raise serializers.ValidationError({"password": "Passwords must match"})

        user = Account(
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            user_type=validated_data["user_type"],
        )

        user.set_password(password)
        user.save()

        Token.objects.create(user=user)
        return user

    def get_token(self, obj):
        token = Token.objects.get(user=obj)
        return token.key


class AdminSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = Account
        fields = (
            "email",
            "first_name",
            "last_name",
            "user_type",
            "phone_number",
            "hospital",
            "password",
            "password2",
        )
        extra_kwargs = {
            "password": {"write_only": True},
            "password2": {"write_only": True},
        }

    def validate(self, data):
        # Check if passwords match
        if data.get("password") != data.get("password2"):
            raise serializers.ValidationError({"password": "Passwords must match"})
        return data

    def create(self, validated_data):
        # Remove password2 from validated_data as it's not needed for the creation
        validated_data.pop("password2")

        # Use the manager's create_user method for better consistency
        user = Account.objects.create_user(
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            user_type=validated_data["user_type"],
            phone_number=validated_data["phone_number"],
            hospital=validated_data.get("hospital"),
            password=validated_data["password"],
        )

        return user


class AdminPropertiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            "id",
            "hospital",
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "user_type"
        ]


class AccountPropertiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "address",
            "region",
            "date_of_birth",
            "profile_image",
        ]
