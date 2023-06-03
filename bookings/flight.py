# bookings/flight.py

from django.db import models
from django.contrib.auth.models import User

class FlightReservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    departure_date = models.DateField()
    passenger_name = models.CharField(max_length=100)
    passenger_email = models.EmailField()
    flight_details = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Flight Reservation #{self.pk}"
