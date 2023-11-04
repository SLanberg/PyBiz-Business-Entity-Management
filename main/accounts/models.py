from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from .validators import establishment_date_validator, validate_id_code_length, validate_share_count, validate_llc_id_code_length


class NaturalPerson(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    id_code = models.CharField(max_length=11, unique=True, validators=[validate_id_code_length])

    def __str__(self):
        return self.first_name + " " + self.last_name + " | " + self.id_code


class LegalEntity(models.Model):
    name = models.CharField(max_length=100)
    registration_code = models.CharField(max_length=7, unique=True, validators=[validate_llc_id_code_length])

    def __str__(self):
        return self.name + " | " + self.registration_code


class LimitedLiabilityCompany(models.Model):
    name = models.CharField(max_length=100)
    registration_code = models.CharField(max_length=7, validators=[validate_llc_id_code_length], unique=True)
    total_capital_size = models.DecimalField(decimal_places=2, max_digits=30, validators=[MinValueValidator(2500)])
    establishment_date = models.DateField(null=False, validators=[establishment_date_validator])
    
    def __str__(self):
        return self.name + " | " + self.registration_code
    

class Shareholder(models.Model):
    natural_person = models.ForeignKey(NaturalPerson, null=True, blank=True, on_delete=models.CASCADE)
    legal_entity = models.ForeignKey(LegalEntity, null=True, blank=True, on_delete=models.CASCADE)
    company = models.ForeignKey(LimitedLiabilityCompany, on_delete=models.CASCADE)
    share_count = models.DecimalField(decimal_places=2, max_digits=30, validators=[validate_share_count])
    is_founder = models.BooleanField(default=True)

    def clean(self):
        # Ensure that only one of natural_person or legal_entity is set
        if self.natural_person and self.legal_entity:
            raise ValidationError("A shareholder can only be associated with either a NaturalPerson or a LegalEntity, not both.")
        if not self.natural_person and not self.legal_entity:
            raise ValidationError("At least one should be chosen.")

    def save(self, *args, **kwargs):
        self.clean()  # Call the clean method to perform validation
        super(Shareholder, self).save(*args, **kwargs)

    def __str__(self):
        if self.natural_person:
            return self.natural_person.first_name + " " + self.natural_person.last_name
        elif self.legal_entity:
            return self.legal_entity.name

