from django.core.management.base import BaseCommand
from accounts.models import LegalEntity, NaturalPerson, LimitedLiabilityCompany, Shareholder
from faker import Faker
import random


class Command(BaseCommand):
    help = 'Populate LegalEntity and create admin user'

    def handle(self, *args, **options):
        fake = Faker()

        # Populate LegalEntity
        legal_entities = []
        for _ in range(5):  # Adjust the number of entities as needed
            name = fake.company()
            registration_code = ''.join(random.choices('0123456789', k=11))
            legal_entity = LegalEntity.objects.create(
                name=name, registration_code=registration_code)
            legal_entities.append(legal_entity)

        # Populate NaturalPerson
        natural_persons = []
        for _ in range(5):  # Adjust the number of persons as needed
            first_name = fake.first_name()
            last_name = fake.last_name()
            id_code = ''.join(random.choices('0123456789', k=11))
            natural_person = NaturalPerson.objects.create(
                first_name=first_name, last_name=last_name, id_code=id_code)
            natural_persons.append(natural_person)


        for _ in range(20):  # Adjust the number of companies as needed
            company_name = fake.company() + " LLC"
            registration_code = ''.join(random.choices('0123456789', k=11))
            establishment_date = fake.date_between(
                start_date='-30y', end_date='today')
            total_capital_size = 6000

            company = LimitedLiabilityCompany.objects.create(
                name=company_name,
                registration_code=registration_code,
                establishment_date=establishment_date,
                total_capital_size=total_capital_size
            )

            # Create Shareholders for the company
            for i in range(3):  # Adjust the number of shareholders as needed
                is_founder = random.choice([True, False])
                share_count = total_capital_size / 3

                if is_founder:
                    # Create Shareholder with a NaturalPerson
                    natural_person = NaturalPerson.objects.order_by(
                        '?').first()
                    Shareholder.objects.create(
                        natural_person=natural_person,
                        company=company,
                        share_count=share_count,
                        is_founder=is_founder
                    )
                else:
                    # Create Shareholder with a LegalEntity
                    legal_entity = LegalEntity.objects.order_by('?').first()
                    Shareholder.objects.create(
                        legal_entity=legal_entity,
                        company=company,
                        share_count=share_count,
                        is_founder=is_founder
                    )

        self.stdout.write(self.style.SUCCESS(
            'Successfully populated LegalEntity and shareholders.'))

# Create admin user
# User.objects.create_superuser('admin', 'admin@example.com', 'admin')
