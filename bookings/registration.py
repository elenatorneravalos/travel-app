# bookings/registration.py

from django.contrib.auth.models import User

def register_user(username, email, password):
    user = User.objects.create_user(username, email, password)
    return user
