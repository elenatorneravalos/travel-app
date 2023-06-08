from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from .models import HotelReservation, FlightReservation, UserProfile

def home(request):
    return render(request, 'base.html')

def user_registration(request):
    if request.method == 'POST':
        # Extract registration details from request payload
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Create a new user
        user = User.objects.create_user(username=username, email=email, password=password)

        # Create a user profile
        profile = UserProfile(user=user)
        profile.save()

        return JsonResponse({'message': 'User registered successfully.'})
    else:
        return JsonResponse({'message': 'Invalid request method.'}, status=400)

def user_login(request):
    if request.method == 'POST':
        # Extract login credentials from request payload
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Login the user
            login(request, user)
            return JsonResponse({'message': 'User logged in successfully.'})
        else:
            return JsonResponse({'message': 'Invalid login credentials.'}, status=401)
    else:
        return JsonResponse({'message': 'Invalid request method.'}, status=400)

def create_hotel_reservation(request):
    if request.method == 'POST':
        # Extract reservation details from request payload
        # ...

        # Process the request and create a new hotel reservation
        # ...

        return JsonResponse({'message': 'Hotel reservation created successfully.'})
    else:
        return JsonResponse({'message': 'Invalid request method.'}, status=400)

def get_reservation_details(request, reservation_id):
    reservation = get_object_or_404(HotelReservation, id=reservation_id)
    # Return the reservation details
    # ...

def update_reservation(request, reservation_id):
    reservation = get_object_or_404(HotelReservation, id=reservation_id)
    if request.method == 'PUT':
        # Extract updated reservation details from request payload
        # ...

        # Process the request and update the reservation
        # ...

        return JsonResponse({'message': 'Reservation updated successfully.'})
    else:
        return JsonResponse({'message': 'Invalid request method.'}, status=400)

def delete_reservation(request, reservation_id):
    reservation = get_object_or_404(HotelReservation, id=reservation_id)
    if request.method == 'DELETE':
        # Process the request and delete the reservation
        # ...

        return JsonResponse({'message': 'Reservation deleted successfully.'})
    else:
        return JsonResponse({'message': 'Invalid request method.'}, status=400)

def create_flight_reservation(request):
    if request.method == 'POST':
        # Extract reservation details from request payload
        # ...

        # Process the request and create a new flight reservation
        # ...

        return JsonResponse({'message': 'Flight reservation created successfully.'})
    else:
        return JsonResponse({'message': 'Invalid request method.'}, status=400)

def get_flight_reservation(request, reservation_id):
    reservation = get_object_or_404(FlightReservation, id=reservation_id)
    # Return the flight reservation details
    # ...

def update_flight_reservation(request, reservation_id):
    reservation = get_object_or_404(FlightReservation, id=reservation_id)
    if request.method == 'PUT':
        # Extract updated reservation details from request payload
        # ...

        # Process the request and update the reservation
        # ...

        return JsonResponse({'message': 'Flight reservation updated successfully.'})
    else:
        return JsonResponse({'message': 'Invalid request method.'}, status=400)

def delete_flight_reservation(request, reservation_id):
    reservation = get_object_or_404(FlightReservation, id=reservation_id)
    if request.method == 'DELETE':
        # Process the request and delete the reservation
        # ...

        return JsonResponse({'message': 'Flight reservation deleted successfully.'})
    else:
        return JsonResponse({'message': 'Invalid request method.'}, status=400)

def get_user_profile(request):
    if request.method == 'GET':
        # Retrieve the user's profile information
        # ...

        return JsonResponse({'message': 'User profile retrieved successfully.'})
    else:
        return JsonResponse({'message': 'Invalid request method.'}, status=400)

def update_user_profile(request):
    if request.method == 'PUT':
        # Extract updated profile details from request payload
        # ...

        # Process the request and update the user's profile
        # ...

        return JsonResponse({'message': 'User profile updated successfully.'})
    else:
        return JsonResponse({'message': 'Invalid request method.'}, status=400)

def my_view(request):
    print(request.META['HTTP_HOST'])
    # Rest of your code
