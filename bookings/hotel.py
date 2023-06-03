# bookings/hotel.py

from django.db import models
from django.contrib.auth.models import User

class HotelReservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    room_quantity = models.PositiveIntegerField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    room_type = models.CharField(max_length=50)
    email = models.EmailField()
    hotel_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Hotel Reservation #{self.pk}"
