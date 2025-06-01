from django.test import TestCase
from django.contrib.auth.models import User
from restaurant.models import Booking
from datetime import date

class BookingModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.booking = Booking.objects.create(
            user=self.user,
            date=date.today(),
            time='12:00:00',
            guests=2
        )

    def test_str_representation(self):
        expected_str = f"Booking for {self.user.username} on {self.booking.date}"
        self.assertEqual(str(self.booking), expected_str)

    def test_booking_creation(self):
        self.assertEqual(self.booking.user, self.user)
        self.assertEqual(self.booking.guests, 2)
