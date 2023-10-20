import re

from django.core.validators import MinLengthValidator, EmailValidator
from rest_framework import serializers

from user.models.account import Account


def validate_username(value):
    if value.isalpha() or value.isdigit():
        raise serializers.ValidationError(
            "Username cannot be all letters or all digits.")
    return value


def validate_unique_username(value):
    if Account.objects.filter(username=value).exists():
        raise serializers.ValidationError("Username already exists.")
    return value


def validate_unique_email(value):
    if Account.objects.filter(email=value).exists():
        raise serializers.ValidationError("Email already exists.")
    return value


def validate_password(value):
    error_messages = []

    if not re.search(r'[A-Z]', value):
        error_messages.append(
            "Password must contain at least one uppercase letter.")
    if not re.search(r'[a-z]', value):
        error_messages.append(
            "Password must contain at least one lowercase letter.")
    if not re.search(r'\d', value):
        error_messages.append("Password must contain at least one digit.")
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', value):
        error_messages.append("Password must contain at least one symbol.")

    if error_messages:
        raise serializers.ValidationError(error_messages)

    return value


class AccountSerializer(serializers.ModelSerializer):
    email = serializers.CharField(
        required=True,
        max_length=50,
        validators=[
            EmailValidator(message="Invalid email format."),
            validate_unique_email
        ]
    )

    username = serializers.CharField(
        required=True,
        max_length=50,
        validators=[
            MinLengthValidator(
                limit_value=3, message="Username must be at least 3 characters long."),
            validate_username,
            validate_unique_username
        ]
    )

    password = serializers.CharField(
        required=True,
        max_length=50,
        validators=[
            MinLengthValidator(
                limit_value=8, message="Password must be at least 8 characters long."),
            validate_password
        ]
    )

    class Meta:
        model = Account
        fields = '__all__'
