from django.db import models
from .validators import validate_integer, validate_id_code_length
from django.core.exceptions import ValidationError

class NaturalPerson(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    id_code = models.CharField(max_length=11, validators=[validate_id_code_length, validate_integer])

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class LegalEntity(models.Model):
    name = models.CharField(max_length=100)
    registration_code = models.CharField(max_length=11, validators=[validate_id_code_length, validate_integer])

    def __str__(self):
        return self.name

class LimitedLiabilityCompany(models.Model):
    name = models.CharField(max_length=100)
    registration_code = models.CharField(max_length=7)
    establishment_date = models.DateField()
    total_capital_size = models.PositiveIntegerField()
    shareholders = models.ManyToManyField('Shareholder', related_name='shareholders')

    def __str__(self):
        return self.name

class Shareholder(models.Model):
    natural_person = models.OneToOneField(
        NaturalPerson,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    legal_entity = models.OneToOneField(
        LegalEntity,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    share_count = models.PositiveIntegerField()
    is_founder = models.BooleanField()
    company = models.ForeignKey(LimitedLiabilityCompany, on_delete=models.CASCADE)

    def __str__(self):
        if self.natural_person:
            return f"Natural Person: {self.natural_person.first_name} {self.natural_person.last_name}"
        elif self.legal_entity:
            return f"Legal Entity: {self.legal_entity.name}"
