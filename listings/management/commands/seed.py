from django.core.management.base import BaseCommand
from listings.models import Listing, Booking, Review
from django.utils import timezone
import random

class Command(BaseCommand):
    help = 'Seed the database with sample listings, bookings, and reviews'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding data...')

        # Sample listings
        listings_data = [
            {"title": "Cozy Apartment", "description": "A cozy place in the city center.", "price": 50.0},
            {"title": "Beach House", "description": "Beautiful view of the sea.", "price": 120.0},
            {"title": "Mountain Cabin", "description": "Escape to the mountains.", "price": 80.0},
        ]

        # Create listings
        for data in listings_data:
            listing, created = Listing.objects.get_or_create(
                title=data["title"],
                defaults={
                    "description": data["description"],
                    "price": data["price"],
                    "created_at": timezone.now()
                }
            )
            if created:
                self.stdout.write(f'Created listing: {listing.title}')

        # Sample bookings and reviews
        listings = Listing.objects.all()
        for listing in listings:
            for i in range(2):  # two sample bookings per listing
                booking = Booking.objects.create(
                    listing=listing,
                    guest_name=f"Guest {random.randint(1,100)}",
                    start_date=timezone.now().date(),
                    end_date=timezone.now().date(),
                    status=random.choice(['pending', 'confirmed', 'canceled'])
                )
                self.stdout.write(f'Created booking for listing: {listing.title}')

                # Sample review for each booking
                review = Review.objects.create(
                    booking=booking,
                    rating=random.randint(1,5),
                    comment="This is a sample review."
                )
                self.stdout.write(f'Created review for booking ID: {booking.id}')

        self.stdout.write(self.style.SUCCESS('Database seeding completed!'))
