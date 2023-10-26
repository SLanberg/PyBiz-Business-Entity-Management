from django.core.exceptions import ValidationError


def validate_integer(value):
    try:
        int(value)
    except ValueError:
        raise ValidationError("id_code must contain only integer digits")


def validate_id_code_length(value):
    if len(value) != 11:
        raise ValidationError("id_code must have exactly 11 characters")