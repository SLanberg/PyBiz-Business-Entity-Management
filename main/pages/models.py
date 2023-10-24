from django.db import models

class LimitedLiabilityCompany(models.Model):
    name = models.CharField(max_length=100)
    registration_code = models.CharField(max_length=7)
    establishment_date = models.DateField()
    total_capital_size = models.PositiveIntegerField()

    def __str__(self):
        return self.name  # You can customize this to display any relevant information

