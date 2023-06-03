
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)

class HotelReservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    room_quantity = models.PositiveIntegerField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    room_type = models.CharField(max_length=100)
    email = models.EmailField()
    hotel_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class FlightReservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    departure_date = models.DateField()
    passenger_name = models.CharField(max_length=100)
    passenger_email = models.EmailField()
    flight_details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
