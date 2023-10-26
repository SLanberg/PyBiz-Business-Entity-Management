from django.db import models
from .validators import validate_id_code_length, validate_integer

class NaturalPerson(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    id_code = models.CharField(max_length=11)


class LegalEntity(models.Model):
    name = models.CharField(max_length=100)
    registration_code = models.CharField(max_length=11)


class LimitedLiabilityCompany(models.Model):
    name = models.CharField(max_length=100)
    registration_code = models.CharField(max_length=7)
    establishment_date = models.DateField()
    total_capital_size = models.PositiveIntegerField()


class Shareholder(models.Model):
    natural_person = models.ForeignKey(NaturalPerson, null=True, blank=True, on_delete=models.CASCADE)
    legal_entity = models.ForeignKey(LegalEntity, null=True, blank=True, on_delete=models.CASCADE)
    company = models.ForeignKey(LimitedLiabilityCompany, null=True, blank=True, on_delete=models.CASCADE)
    share_count = models.PositiveIntegerField()
    is_founder = models.BooleanField(default=True)