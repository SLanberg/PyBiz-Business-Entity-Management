from django.db import models, IntegrityError
from django.core.validators import MinValueValidator
from .validators import establishment_date_validator
from django.db.models import Q


class NaturalPerson(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    id_code = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return self.first_name + " " + self.last_name + " | " + self.id_code


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
    establishment_date = models.DateField(
        validators=[establishment_date_validator])

    def __str__(self):
        return self.name + " | " + self.registration_code


class Shareholder(models.Model):
    natural_person = models.ForeignKey(
        NaturalPerson, null=True, blank=True, on_delete=models.CASCADE)
    legal_entity = models.ForeignKey(
        LegalEntity, null=True, blank=True, on_delete=models.CASCADE)
    company = models.ForeignKey(
        LimitedLiabilityCompany, null=True, blank=True, on_delete=models.CASCADE)
    share_count = models.PositiveIntegerField()
    is_founder = models.BooleanField(default=True)

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=~Q(natural_person__isnull=False,
                         legal_entity__isnull=False),
                name="either_natural_person_or_legal_entity"
            )
        ]

    def save(self, *args, **kwargs):
        # Ensure that only one of natural_person or legal_entity is set
        if self.natural_person and self.legal_entity:
            raise IntegrityError(
                "A shareholder can only be associated with either a NaturalPerson or a LegalEntity, not both.")
        super(Shareholder, self).save(*args, **kwargs)
