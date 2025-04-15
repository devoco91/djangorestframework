# accounts/management/commands/createadmin.py
import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = "Create or update a Django superuser using environment variables"

    def add_arguments(self, parser):
        parser.add_argument(
            '--force', action='store_true', help='Force update password if user exists'
        )

    def handle(self, *args, **options):
        User = get_user_model()

        username = os.getenv("ADMIN_USERNAME", "admin")
        email = os.getenv("ADMIN_EMAIL", "admin@example.com")
        password = os.getenv("ADMIN_PASSWORD", "Official@lasop1")
        force_update = options['force']

        user = User.objects.filter(username=username).first()

        if user:
            if force_update:
                user.set_password(password)
                user.email = email
                user.save()
                self.stdout.write(self.style.WARNING("⚠️  Superuser password updated."))
            else:
                self.stdout.write("ℹ️ Superuser already exists. Use --force to update.")
        else:
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS("✅ Superuser created."))
