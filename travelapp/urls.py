from django.urls import path
from bookings import views

urlpatterns = [
    path('', views.home, name='home'),
    # User Registration
    path('api/register/', views.user_registration),
    # User Login
    path('api/login/', views.user_login),
    # Hotel Reservation
    path('api/hotelreservations/', views.create_hotel_reservation),
    path('api/reservations/<int:reservation_id>/', views.get_reservation_details),
    path('api/hotelreservations/<int:reservation_id>/update/', views.update_reservation),
    path('api/hotelreservations/<int:reservation_id>/delete/', views.delete_reservation),
    # Flight Reservation
    path('api/flightreservations/', views.create_flight_reservation),
    path('api/flightreservations/<int:reservation_id>/', views.get_flight_reservation),
    path('api/flightreservations/<int:reservation_id>/update/', views.update_flight_reservation),
    path('api/flightreservations/<int:reservation_id>/delete/', views.delete_flight_reservation),
    # User Profile
    path('api/profile/', views.get_user_profile),
    path('api/profile/update/', views.update_user_profile),
]
