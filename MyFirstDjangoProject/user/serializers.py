


















from rest_framework import serializers
from .models import Profile
from django.core import validators
from django.core.exceptions import ValidationError
from django.utils import timezone

def validate_date_of_birth(value):
    if value >= timezone.now().date():
        raise ValidationError('Date of birth must not be in the future.')


class ProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(
        max_length=50,
        validators=[
            validators.RegexValidator(
                regex='^[A-Za-z]*$',
                message='First name must only contain alphabetic characters.',
                code='invalid_first_name'
            ),
        ]
    )
    
    last_name = serializers.CharField(
        max_length=50,
        validators=[
            validators.MinLengthValidator(limit_value=2, message='Last name must be at least 2 characters long.'),
        ]
    )
    
    phone_number = serializers.CharField(
        max_length=20,
        validators=[
            validators.RegexValidator(
                regex='^\d+$',
                message='Phone number must contain only digits.',
                code='invalid_phone_number'
            ),
        ]
    )

    date_of_birth = serializers.DateField(
        validators=[validate_date_of_birth]
    )

    
    class Meta:
        model = Profile
        fields = '__all__'
