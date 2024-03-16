from django.test import TestCase
from tixx.models import Arena, Event, Ticket, User, Payment, Review, Seat, Figure, Admin

# Tests for each model

class ModelTestCase(TestCase):
    def setUp(self):
        self.arena = Arena.objects.create(
            arenaName="Test Arena",
            arenaCapacity=2
        )
        self.event = Event.objects.create(
            eventName="Test Event",
            eventDate="2024-03-10",
            eventLocation="Test Location",
            eventDescription="Test Description",
            eventStatus="Upcoming",
            eventGenre="Test Genre",
            arenaId = self.arena
        )
        self.ticket = Ticket.objects.create(
            eventId=self.event,
            seatNum="A1",
            arenaId = self.arena,
            ticketQR="test_qr_code",
            ticketPrice=50,
            ticketType="Regular"
        )
        self.user = User.objects.create(
            userId="test_user",
            username="Test User",
            userEmail="test@example.com",
            userPhoneNumber="1234567890",
            userAddress="Test Address"
        )
        self.payment = Payment.objects.create(
            paymentId="test_payment",
            userId=self.user,
            paymentAmount=100.00,
            paymentMethod="Credit Card",
            paymentDate="2024-03-09",
            transactionId="1234567890"
        )
        self.review = Review.objects.create(
            reviewRating=5,
            reviewTitle="Great Event",
            reviewText="Drake was great!!!",
            eventID=self.event,
            reviewDate="2024-03-09"
        )

    def test_arena_str(self):
        self.assertEqual(str(self.arena), "Test Arena")

    def test_event_str(self):
        self.assertEqual(str(self.event), "Test Event")

    def test_ticket_str(self):
        self.assertEqual(str(self.ticket), "A1")

    def test_user_str(self):
        self.assertEqual(str(self.user), "Test User")

    def test_payment_str(self):
        self.assertEqual(str(self.payment), "test_payment")

    def test_review_str(self):
        self.assertEqual(str(self.review), "Great Event")
    
    
    
