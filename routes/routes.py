from django.urls import path
from controllers.bookings_controller import BookingController
from controllers.user_controller import UserController
from controllers.rooms_controller import RoomsController
from controllers.payments_controller import PaymentsController
from controllers.tariffs_controller import TariffsController

urlpatterns = [
    path('bookings/', BookingController.as_view(), name='create-booking'),
    path('users/', UserController.as_view(), name='create-user'),
    path('rooms/', RoomsController.as_view(), name='create-room'),
    path('payments/', PaymentsController.as_view(), name='create-payment'),
    path('tariffs/', TariffsController.as_view(), name='create-tariff'),
]
