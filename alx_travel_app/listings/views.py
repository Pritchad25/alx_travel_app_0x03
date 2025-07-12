from django.shortcuts import render
from listings.tasks import send_booking_confirmation_email

# After booking is created
send_booking_confirmation_email.delay(booking.customer.email, booking.id)
# Create your views here.
