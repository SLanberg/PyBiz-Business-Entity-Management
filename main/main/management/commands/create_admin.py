from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create admin user'

    def handle(self, *args, **options):
        admin_username = 'admin'
        admin_email = 'admin@example.com'
        admin_password = 'admin'

        # Check if the admin user already exists
        if User.objects.filter(username=admin_username).exists():
            self.stdout.write(self.style.WARNING('Admin user already exists. Skipping.'))
        else:
            # Create the admin user
            admin_user = User.objects.create_superuser(admin_username, admin_email, admin_password)
            self.stdout.write(self.style.SUCCESS(f'Admin user "{admin_username}" created with email "{admin_email}"'))

