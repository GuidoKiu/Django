from rest_framework import serializers
from user.models.profile import Profile
from django.core import validators
from django.core.exceptions import ValidationError
from django.utils import timezone

def validate_date_of_birth(value):
    if value >= timezone.now().date():
        raise ValidationError('Date of birth must not be in the future.')

def validate_unique_phone_numbers(value):
    if Profile.objects.filter(phone_number=value).exists():
        raise ValidationError("Phone number already registered under a profile.")

class ProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(
        required=True,
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
        required=False,
        max_length=50,
        validators=[
            validators.MinLengthValidator(limit_value=2, message='Last name must be at least 2 characters long.'),
        ]
    )
    
    phone_number = serializers.CharField(
        required=False,
        max_length=20,
        validators=[
            validate_unique_phone_numbers,
            validators.RegexValidator(
                regex='^\d+$',
                message='Phone number must contain only digits.',
                code='invalid_phone_number'
            ),
        ]
    )

    date_of_birth = serializers.DateField(
        required=False,
        validators=[validate_date_of_birth]
    )

    
    class Meta:
        model = Profile
        fields = '__all__'
