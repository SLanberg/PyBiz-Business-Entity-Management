from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_integer(value):
    try:
        int(value)
    except ValueError:
        raise ValidationError("id_code must contain only integer digits")

def validate_id_code_length(value):
    if len(value) != 11:
        raise ValidationError("Must have exactly 11 numbers")
    

def validate_llc_id_code_length(value):
    if len(value) != 7:
        raise ValidationError("Must have exactly 7 numbers")

def establishment_date_validator(value):
    if value > timezone.now().date():
        raise ValidationError(
            "Establishment date cannot exceed the current date")

def validate_share_count(value):
    if value <= 0:
        raise ValidationError("Share count must be greater than 0")