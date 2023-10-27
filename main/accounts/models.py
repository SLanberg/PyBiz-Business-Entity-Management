from django.db import models
from django.core.validators import MinValueValidator
from .validators import establishment_date_validator

class NaturalPerson(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    id_code = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return self.first_name + " " + self.last_name + " | " +self.id_code

class LegalEntity(models.Model):
    name = models.CharField(max_length=100)
    registration_code = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return self.name + " | " + self.registration_code


class LimitedLiabilityCompany(models.Model):
    name = models.CharField(max_length=100)
    registration_code = models.CharField(max_length=7, unique=True)
    establishment_date = models.DateField()
    total_capital_size = models.PositiveIntegerField(
        validators=[MinValueValidator(2500)]
    )
    establishment_date = models.DateField(validators=[establishment_date_validator])

    def __str__(self):
        return self.name + " | " + self.registration_code


class Shareholder(models.Model):
    natural_person = models.ForeignKey(NaturalPerson, null=True, blank=True, on_delete=models.CASCADE)
    legal_entity = models.ForeignKey(LegalEntity, null=True, blank=True, on_delete=models.CASCADE)
    company = models.ForeignKey(LimitedLiabilityCompany, null=True, blank=True, on_delete=models.CASCADE)
    share_count = models.PositiveIntegerField()
    is_founder = models.BooleanField(default=True)
