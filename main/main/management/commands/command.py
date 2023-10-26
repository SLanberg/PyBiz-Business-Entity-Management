from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from accounts.models import LegalEntity
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Populate LegalEntity and create admin user'

    def handle(self, *args, **options):
        fake = Faker()

        # Create admin user
        User.objects.create_superuser('admin', 'admin@example.com', 'admin')

        # Populate LegalEntity
        for _ in range(10):  # Adjust the number of entities as needed
            name = fake.company()
            registration_code = ''.join(random.choices('0123456789', k=11))
            LegalEntity.objects.create(name=name, registration_code=registration_code)

        self.stdout.write(self.style.SUCCESS('Successfully populated LegalEntity and created admin user.'))
