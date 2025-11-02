from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os

class Command(BaseCommand):
    help = (
        "Create a demo user if it does not exist. "
        "Uses environment variables: DEMO_USER_EMAIL, DEMO_USER_PASSWORD, optional DEMO_USER_USERNAME."
    )

    def handle(self, *args, **options):
        User = get_user_model()
        email = os.environ.get('DEMO_USER_EMAIL', 'demo@example.com')
        password = os.environ.get('DEMO_USER_PASSWORD', 'demopassword')
        username = os.environ.get('DEMO_USER_USERNAME') or email.split('@')[0]

        if User.objects.filter(email=email).exists() or User.objects.filter(username=username).exists():
            self.stdout.write(self.style.WARNING(f"Demo user already exists (email={email}, username={username})."))
            return

        try:
            User.objects.create_user(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f"Demo user created: username={username}, email={email}"))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Failed to create demo user: {e}"))