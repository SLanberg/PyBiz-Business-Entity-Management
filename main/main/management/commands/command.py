from django.core.management.base import BaseCommand
from pages.models import LimitedLiabilityCompany
from faker import Faker
from random import randint
from datetime import date, timedelta

class Command(BaseCommand):
    help = 'Populate the LimitedLiabilityCompany model with dummy data'

    def handle(self, *args, **options):
        fake = Faker()

        for _ in range(100):  # Change 100 to the desired number of records
            llc = LimitedLiabilityCompany(
                name=fake.company(),
                registration_code=fake.unique.random_number(digits=7),
                establishment_date=fake.date_between(start_date='-30y', end_date='today'),
                total_capital_size=randint(1000, 1000000)
            )
            llc.save()

        self.stdout.write(self.style.SUCCESS('Limited Liability Companies have been populated successfully. ✅'))
