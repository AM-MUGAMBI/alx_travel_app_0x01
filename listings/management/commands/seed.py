from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from listings.models import Listing
import random

class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **kwargs):
        if not User.objects.exists():
            self.stdout.write(self.style.WARNING('No users found. Creating default users...'))
            for i in range(3):
                User.objects.create_user(username=f'user{i}', password='pass1234')

        users = list(User.objects.all())

        locations = ['New York', 'Paris', 'Tokyo', 'London', 'Berlin']
        titles = ['Cozy Apartment', 'Modern Studio', 'Beach House', 'Mountain Cabin', 'Luxury Suite']
        descriptions = [
            'A lovely place to stay.',
            'Close to all amenities.',
            'Perfect for a weekend getaway.',
            'Spacious and well-lit.',
            'Recently renovated.'
        ]

        for _ in range(10):
            Listing.objects.create(
                title=random.choice(titles),
                description=random.choice(descriptions),
                location=random.choice(locations),
                price_per_night=random.randint(50, 500),
                host=random.choice(users)
            )

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database with listings!'))

